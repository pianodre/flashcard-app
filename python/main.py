from deck import Deck
from flashcard import Flashcard
from deckManager import DeckManager

def main():
    deck_manager = DeckManager()

    deck_names = deck_manager.list_decks()

    print("Select a deck to study: ")
    for deck_name in deck_names:
        print(deck_name)
    
    selected_deck = input()
    print("\n")

    current_deck = deck_manager.load_deck(selected_deck)

    for card in current_deck.cards:
        print(card.get_question() + "| Difficulty: " + str(card.get_difficulty()))
        input("Press Enter to see the answer...")
        print(card.get_answer())

        print("Select a difficulty level: ")
        new_difficulty = input()
        if new_difficulty != "1" and new_difficulty != "2" and new_difficulty != "3":
            new_difficulty = card.get_difficulty()

        card.edit_flashcard(card.get_question(), card.get_answer(), int(new_difficulty))
        input("Press Enter to continue...")
    
    deck_manager.save_deck(current_deck)

    
if __name__ == "__main__":
    main()
