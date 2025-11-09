from deck import Deck
from flashcard import Flashcard
from deckManager import DeckManager
from ioControl import IOControl
from testFunctions import *

def main():
    """Main menu for flashcard app"""
    while True:
        print("\n🎴 Flashcard App")
        print("=" * 30)
        print("1. Study a deck (test_deck)")
        print("2. Manage decks (create/edit/delete)")
        print("3. Import/Export .txt files")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == "1":
            test_deck()
        elif choice == "2":
            manage_decks()
        elif choice == "3":
            test_import_export()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
