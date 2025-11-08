from deck import Deck
from flashcard import Flashcard
from deckManager import DeckManager
from ioControl import IOControl

def manage_decks():
    """Interactive deck management menu"""
    deck_manager = DeckManager()
    
    while True:
        print("\n🗂️  Deck Management")
        print("=" * 35)
        print("1. Create new deck")
        print("2. View all decks")
        print("3. Edit deck (add/remove cards)")
        print("4. Delete deck")
        print("5. Back to main menu")
        
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == "1":
            _create_new_deck(deck_manager)
        elif choice == "2":
            _view_all_decks(deck_manager)
        elif choice == "3":
            _edit_deck(deck_manager)
        elif choice == "4":
            _delete_deck(deck_manager)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, 4, or 5.")

def _create_new_deck(deck_manager):
    """Create a new deck with cards"""
    deck_name = input("\nEnter name for new deck: ").strip()
    if not deck_name:
        print("Deck name cannot be empty!")
        return
    
    new_deck = Deck(deck_name)
    
    print(f"\nCreating deck: '{deck_name}'")
    print("Add flashcards (press Enter with empty question to finish):")
    
    while True:
        question = input("\nQuestion: ").strip()
        if not question:
            break
        
        answer = input("Answer: ").strip()
        if not answer:
            print("Answer cannot be empty!")
            continue
        
        while True:
            difficulty = input("Difficulty (1-Easy, 2-Medium, 3-Hard) [1]: ").strip()
            if not difficulty:
                difficulty = 1
                break
            try:
                difficulty = int(difficulty)
                if difficulty in [1, 2, 3]:
                    break
                else:
                    print("Please enter 1, 2, or 3")
            except ValueError:
                print("Please enter a valid number")
        
        card = Flashcard(question, answer, difficulty)
        new_deck.add_flashcard(card)
        print(f"✓ Added card ({len(new_deck.cards)} total)")
    
    if new_deck.cards:
        deck_manager.create_deck(new_deck)
        print(f"\n✅ Deck '{deck_name}' created with {len(new_deck.cards)} cards!")
    else:
        print("\n❌ No cards added. Deck not created.")

def _view_all_decks(deck_manager):
    """Display all decks with their statistics"""
    deck_names = deck_manager.list_decks()
    
    if not deck_names:
        print("\nNo decks found!")
        return
    
    print(f"\n📚 All Decks ({len(deck_names)} total):")
    print("-" * 50)
    
    for i, deck_file in enumerate(deck_names, 1):
        deck_name = deck_file.replace('.json', '')
        deck = deck_manager.load_deck(deck_name)
        
        if deck:
            clean_name = deck.name
            card_count = len(deck.cards)
            difficulties = [card.get_difficulty() for card in deck.cards]
            easy_count = difficulties.count(1)
            medium_count = difficulties.count(2)
            hard_count = difficulties.count(3)
            
            print(f"{i}. {clean_name}")
            print(f"   Cards: {card_count} (Easy: {easy_count}, Medium: {medium_count}, Hard: {hard_count})")
        else:
            print(f"{i}. {deck_name} (Error loading)")

def _edit_deck(deck_manager):
    """Edit a deck by adding or removing cards"""
    deck_names = deck_manager.list_decks()
    
    if not deck_names:
        print("\nNo decks found!")
        return
    
    print("\nSelect deck to edit:")
    for i, deck_name in enumerate(deck_names, 1):
        clean_name = deck_name.replace('.json', '').replace('_', ' ').title()
        print(f"{i}. {clean_name}")
    
    try:
        choice = int(input("\nSelect deck number: ")) - 1
        if choice < 0 or choice >= len(deck_names):
            print("Invalid selection!")
            return
        
        selected_deck_name = deck_names[choice].replace('.json', '')
        deck = deck_manager.load_deck(selected_deck_name)
        
        if not deck:
            print("Failed to load deck!")
            return
        
        while True:
            print(f"\n📝 Editing: {deck.name}")
            print("=" * 40)
            print("1. Add new card")
            print("2. Remove card")
            print("3. View all cards")
            print("4. Save and exit")
            
            edit_choice = input("\nSelect option (1-4): ").strip()
            
            if edit_choice == "1":
                _add_card_to_deck(deck_manager, deck)
            elif edit_choice == "2":
                _remove_card_from_deck(deck_manager, deck)
            elif edit_choice == "3":
                _view_deck_cards(deck)
            elif edit_choice == "4":
                deck_manager.save_deck(deck)
                print(f"✅ Deck '{deck.name}' saved!")
                break
            else:
                print("Invalid choice!")
                
    except ValueError:
        print("Please enter a valid number!")

def _add_card_to_deck(deck_manager, deck):
    """Add a new card to existing deck"""
    question = input("\nQuestion: ").strip()
    if not question:
        print("Question cannot be empty!")
        return
    
    answer = input("Answer: ").strip()
    if not answer:
        print("Answer cannot be empty!")
        return
    
    while True:
        difficulty = input("Difficulty (1-Easy, 2-Medium, 3-Hard) [1]: ").strip()
        if not difficulty:
            difficulty = 1
            break
        try:
            difficulty = int(difficulty)
            if difficulty in [1, 2, 3]:
                break
            else:
                print("Please enter 1, 2, or 3")
        except ValueError:
            print("Please enter a valid number")
    
    card = Flashcard(question, answer, difficulty)
    deck_manager.add_flashcard(deck, card)
    print(f"✅ Card added! Deck now has {len(deck.cards)} cards.")

def _remove_card_from_deck(deck_manager, deck):
    """Remove a card from existing deck"""
    if not deck.cards:
        print("No cards in this deck!")
        return
    
    print("\nCards in deck:")
    for i, card in enumerate(deck.cards, 1):
        print(f"{i}. Q: {card.get_question()}")
        print(f"   A: {card.get_answer()}")
    
    try:
        choice = int(input(f"\nSelect card to remove (1-{len(deck.cards)}): ")) - 1
        if choice < 0 or choice >= len(deck.cards):
            print("Invalid selection!")
            return
        
        card_to_remove = deck.cards[choice]
        deck_manager.remove_flashcard(deck, card_to_remove)
        print(f"✅ Card removed! Deck now has {len(deck.cards)} cards.")
        
    except ValueError:
        print("Please enter a valid number!")

def _view_deck_cards(deck):
    """Display all cards in a deck"""
    if not deck.cards:
        print("No cards in this deck!")
        return
    
    print(f"\n📋 Cards in '{deck.name}' ({len(deck.cards)} total):")
    print("-" * 50)
    
    for i, card in enumerate(deck.cards, 1):
        difficulty_text = {1: "Easy", 2: "Medium", 3: "Hard"}[card.get_difficulty()]
        print(f"{i}. Q: {card.get_question()}")
        print(f"   A: {card.get_answer()}")
        print(f"   Difficulty: {difficulty_text}")
        print()

def _delete_deck(deck_manager):
    """Delete a deck"""
    deck_names = deck_manager.list_decks()
    
    if not deck_names:
        print("\nNo decks found!")
        return
    
    print("\nSelect deck to delete:")
    for i, deck_name in enumerate(deck_names, 1):
        clean_name = deck_name.replace('.json', '').replace('_', ' ').title()
        print(f"{i}. {clean_name}")
    
    try:
        choice = int(input("\nSelect deck number: ")) - 1
        if choice < 0 or choice >= len(deck_names):
            print("Invalid selection!")
            return
        
        selected_deck_name = deck_names[choice].replace('.json', '')
        deck = deck_manager.load_deck(selected_deck_name)
        
        if deck:
            deck_manager.remove_deck(deck)
        else:
            print("Failed to load deck!")
            
    except ValueError:
        print("Please enter a valid number!")

def test_deck():
    """Loop through a deck and allow editing difficulty of each flashcard"""
    deck_manager = DeckManager()
    
    # List available decks
    deck_names = deck_manager.list_decks()
    
    if not deck_names:
        print("No decks found!")
        return
    
    print("Available decks:")
    for i, deck_name in enumerate(deck_names, 1):
        clean_name = deck_name.replace('.json', '').replace('_', ' ').title()
        print(f"{i}. {clean_name}")
    
    # Get user's deck selection
    try:
        choice = int(input("\nSelect a deck number: ")) - 1
        if choice < 0 or choice >= len(deck_names):
            print("Invalid selection!")
            return
        
        selected_deck_file = deck_names[choice]
        selected_deck_name = selected_deck_file.replace('.json', '')
        
    except ValueError:
        print("Please enter a valid number!")
        return
    
    # Load the selected deck
    current_deck = deck_manager.load_deck(selected_deck_name)
    if not current_deck:
        print("Failed to load deck!")
        return
    
    # Get due cards and show statistics
    due_cards = current_deck.get_due_cards()
    total_cards = len(current_deck.cards)
    due_count = len(due_cards)
    
    print(f"\n=== Studying Deck: {current_deck.name} ===")
    print(f"Total cards: {total_cards}")
    print(f"Due for review: {due_count}")
    
    # Ask user what they want to study
    if due_count > 0:
        print(f"\nStudy options:")
        print(f"1. Study due cards only ({due_count} cards)")
        print(f"2. Study all cards ({total_cards} cards)")
        
        while True:
            study_choice = input("\nSelect study option (1-2): ").strip()
            if study_choice == "1":
                cards_to_study = due_cards
                break
            elif study_choice == "2":
                cards_to_study = current_deck.cards
                break
            else:
                print("Please enter 1 or 2.")
    else:
        print(f"\n✅ No cards are due for review right now!")
        print(f"Study all cards anyway? (y/n)")
        if input().lower().startswith('y'):
            cards_to_study = current_deck.cards
        else:
            print("Come back later when cards are due for review!")
            return
    
    if not cards_to_study:
        print("No cards to study!")
        return
    
    print(f"\n🎯 Starting study session with {len(cards_to_study)} cards\n")
    
    # Loop through each flashcard
    for i, card in enumerate(cards_to_study, 1):
        print(f"Card {i}/{len(cards_to_study)}")
        print("-" * 40)
        print(f"Question: {card.get_question()}")
        print(f"Current Difficulty: {card.get_difficulty()}")
        
        # Show next review info if it exists
        if hasattr(card, 'next_review') and card.next_review:
            from datetime import datetime
            try:
                next_review_time = datetime.fromisoformat(card.next_review)
                print(f"Next review: {next_review_time.strftime('%Y-%m-%d %H:%M:%S')}")
            except:
                print("Next review: Not set")
        
        input("\nPress Enter to see the answer...")
        print(f"Answer: {card.get_answer()}")
        
        # Prompt for difficulty change
        print("\nRate this card:")
        print("1 - Hard (review in 30 seconds)")
        print("2 - Medium (review in 5 minutes)") 
        print("3 - Easy (review tomorrow)")
        
        while True:
            new_difficulty = input(f"Enter difficulty (1-3) or press Enter to keep current ({card.get_difficulty()}): ").strip()
            
            if new_difficulty == "":
                # Keep current difficulty but still update next_review
                card.edit_flashcard(card.get_question(), card.get_answer(), card.get_difficulty())
                break
            elif new_difficulty in ["1", "2", "3"]:
                old_difficulty = card.get_difficulty()
                card.edit_flashcard(card.get_question(), card.get_answer(), int(new_difficulty))
                print(f"Difficulty changed from {old_difficulty} to {new_difficulty}")

                deck_manager.save_deck(current_deck)  # Save immediately after each card
                
                # Show when this card will be reviewed next
                if hasattr(card, 'next_review') and card.next_review:
                    try:
                        next_review_time = datetime.fromisoformat(card.next_review)
                        print(f"📅 Last reviewed: {next_review_time.strftime('%Y-%m-%d %H:%M:%S')}")
                    except:
                        pass
                break
            else:
                print("Please enter 1, 2, 3, or press Enter to keep current difficulty.")
        
        print("\n" + "="*50 + "\n")
    
    # Save the deck with any changes
    deck_manager.save_deck(current_deck)
    print(f"\nDeck '{current_deck.name}' has been saved with any changes!")

def test_import_export():
    """Test the import/export functionality for text files"""
    io_control = IOControl()
    
    while True:
        print("\n🃏 Flashcard Import/Export Utility")
        print("=" * 45)
        print("1. Import from .txt file")
        print("2. Export deck to .txt file")
        print("3. Back to main menu")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == "1":
            io_control.import_txt_file()
        elif choice == "2":
            io_control.export_deck_to_txt()
        elif choice == "3":
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")