from flask import Blueprint, render_template, jsonify, request
import sys, os

# Add your src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from deckManager import DeckManager
from deck import Deck
from flashcard import Flashcard

main = Blueprint('main', __name__)
deck_manager = DeckManager()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/study')
def study():
    return render_template('study.html')

@main.route('/study/<deck_name>')
def study_deck(deck_name):
    return render_template('flashcard.html', deck_name=deck_name)

@main.route('/api/decks')
def get_decks():
    """Get all available decks with statistics"""
    try:
        deck_filenames = deck_manager.list_decks()  # Returns list of filenames
        deck_data = []
        
        for filename in deck_filenames:
            # Remove .json extension to get deck name
            deck_name = filename.replace('.json', '')
            
            # Load each deck to get statistics
            deck = deck_manager.load_deck(deck_name)
            if deck:
                # Get due cards count
                due_cards = len(deck.get_due_cards())
                total_cards = len(deck.cards)
                
                deck_info = {
                    'name': deck.name,
                    'total_cards': total_cards,
                    'due_cards': due_cards,
                    'description': f"{total_cards} cards • {due_cards} due for review"
                }
                deck_data.append(deck_info)
            
        return jsonify({'decks': deck_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/api/study/<deck_name>')
def get_study_cards(deck_name):
    try:
        deck = deck_manager.load_deck(deck_name)
        
        if not deck:
            return jsonify({'error': 'Deck not found'}), 404
        
        cards = deck.get_due_cards()
        
        card_data = []
        for i, card in enumerate(cards):
            card_info = {
                'id': i,  # Add card index for difficulty updates
                'question': card.get_question(),
                'answer': card.get_answer(),
                'difficulty': card.get_difficulty()
            }
            card_data.append(card_info)
        
        return jsonify({
            'deck_name': deck.name,
            'cards': card_data,
            'total_due': len(cards)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/api/card/difficulty', methods=['POST'])
def update_card_difficulty():
    try:
        data = request.get_json() # get JSON data from request
        print(f"DEBUG: Received data: {data}")
        
        if not all(key in data for key in ['deck_name', 'card_index', 'difficulty']):
            return jsonify({'error': 'Missing required parameters'}), 400

        deck = deck_manager.load_deck(data['deck_name']) # load deck
        print(f"DEBUG: Loaded deck: {deck.name if deck else 'None'}")
        if not deck:
            return jsonify({'error': 'Deck not found'}), 404
            
        print(f"DEBUG: Deck has {len(deck.cards)} cards, requesting index {data['card_index']}")
        if data['card_index'] >= len(deck.cards):
            return jsonify({'error': 'Card not found'}), 404
            
        card = deck.cards[data['card_index']] # get card
        print(f"DEBUG: Found card: {card.question}")
        # Only update difficulty, keep existing question and answer
        card.edit_flashcard(card.question, card.answer, data['difficulty']) # update card difficulty

        deck_manager.save_deck(deck) # save deck

        return jsonify({'success': True}) # return success
    except Exception as e:
        print(f"DEBUG: Exception occurred: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@main.route('/api/deck/create', methods=['POST'])
def create_deck():
    try:
        data = request.get_json() # get JSON data from request
        
        if not data or 'deck_name' not in data:
            return jsonify({'error': 'Missing deck_name parameter'}), 400

        new_deck = Deck(data['deck_name']) # create deck object
        deck_manager.create_deck(new_deck) # create deck
        return jsonify({'success': True, 'deck_name': data['deck_name']}) # return success
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/api/deck/<deck_name>/add-card', methods=['POST'])
def add_card_to_deck(deck_name):
    try:
        data = request.get_json() # get JSON data from request
        
        if not all(key in data for key in ['question', 'answer', 'difficulty']):
            return jsonify({'error': 'Missing required parameters'}), 400
        
        deck = deck_manager.load_deck(deck_name) # load deck
        if not deck:
            return jsonify({'error': 'Deck not found'}), 404
            
        new_card = Flashcard(data['question'], data['answer'], data['difficulty']) # create flashcard
        deck_manager.add_flashcard(deck, new_card) # add card to deck
        return jsonify({'success': True, 'card_added': True}) # return success
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/api/deck/<deck_name>/delete', methods=['DELETE'])
def delete_deck(deck_name):
    try:
        deck = deck_manager.load_deck(deck_name) # load deck
        if not deck:
            return jsonify({'error': 'Deck not found'}), 404
            
        deck_manager.remove_deck(deck) # delete deck
        return jsonify({'success': True, 'deck_deleted': deck_name}) # return success
    except Exception as e:
        return jsonify({'error': str(e)}), 500
