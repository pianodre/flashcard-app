''' This class is responsible for
    managing decks of flashcards.

    This class is responsible for 
    - creating, loading, and saving decks
    - adding and removing flashcards
    - deleting decks
    - listing all decks
    IN MEMORY.

    It will eventually become the main menu GUI 
'''

import json
import os
from deck import Deck
from flashcard import Flashcard

class DeckManager:
    def __init__(self):
        self.decks_folder = "decks"
        self.ensure_decks_folder()

    def ensure_decks_folder(self):
        """Create decks folder if it doesn't exist"""
        if not os.path.exists(self.decks_folder):
            os.makedirs(self.decks_folder)

    def save_deck(self, deck):
        """Save deck object to JSON file"""
        try:
            # Convert deck to dictionary
            deck_data = {
                "name": deck.name,
                "created_date": deck.created_date,
                "last_studied": deck.last_studied,
                "cards": []
            }
            
            # Convert each flashcard to dictionary using the to_dict method
            for card in deck.cards:
                deck_data["cards"].append(card.to_dict())
            
            # Create filename from deck name (replace spaces with underscores)
            filename = deck.name.lower().replace(" ", "_") + ".json"
            file_path = os.path.join(self.decks_folder, filename)
            
            # Write to JSON file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(deck_data, f, indent=2, ensure_ascii=False)
            
            print(f"Deck '{deck.name}' saved successfully!")
            return True
            
        except Exception as e:
            print(f"Error saving deck: {e}")
            return False  

    def load_deck(self, deck_name):
        """Load deck from JSON file and return Deck object"""
        try:
            # Create filename (add .json if not present)
            if not deck_name.endswith('.json'):
                filename = deck_name + '.json'
            else:
                filename = deck_name
                deck_name = deck_name[:-5]  # Remove .json for deck name
            
            file_path = os.path.join(self.decks_folder, filename)
            
            # Check if file exists
            if not os.path.exists(file_path):
                print(f"Deck '{deck_name}' not found.")
                return None
            
            # Load JSON data
            with open(file_path, 'r', encoding='utf-8') as f:
                deck_data = json.load(f)
            
            # Create new Deck object
            loaded_deck = Deck(deck_data['name'])
            loaded_deck.created_date = deck_data.get('created_date', loaded_deck.created_date)
            loaded_deck.last_studied = deck_data.get('last_studied', loaded_deck.last_studied)
            
            # Load all flashcards
            for card_data in deck_data['cards']:
                flashcard = Flashcard(
                    card_data['question'],
                    card_data['answer'],
                    card_data['difficulty'],
                    card_data.get('times_studied', 0),
                    card_data.get('last_review', None)
                )
                # Set next_review separately since it's not a constructor parameter
                flashcard.next_review = card_data.get('next_review', None)
                loaded_deck.add_flashcard(flashcard)
            
            print(f"Deck '{deck_data['name']}' loaded successfully! ({len(loaded_deck.cards)} cards)")
            return loaded_deck
            
        except Exception as e:
            print(f"Error loading deck '{deck_name}': {e}")
            return None

    def create_deck(self, deck):
        self.save_deck(deck)

    def remove_deck(self, deck):
        """Remove deck file from storage with safety checks and confirmation"""
        try:
            # Create filename (handle spaces and special characters)
            filename = deck.name.lower().replace(" ", "_") + ".json"
            file_path = os.path.join(self.decks_folder, filename)
            
            # SECURITY: Ensure the file path is within the decks folder
            abs_decks_folder = os.path.abspath(self.decks_folder)
            abs_file_path = os.path.abspath(file_path)
            
            if not abs_file_path.startswith(abs_decks_folder):
                print("Error: Invalid file path. Can only delete files in decks folder.")
                return False
            
            # SECURITY: Ensure it's a .json file
            if not filename.endswith('.json'):
                print("Error: Can only delete .json files.")
                return False
            
            # Check if file exists
            if not os.path.exists(file_path):
                print(f"Deck '{deck.name}' not found.")
                return False
            
            # CONFIRMATION: Ask user to confirm deletion
            print(f"Are you sure you want to delete deck '{deck.name}'?")
            print("This action cannot be undone.")
            confirmation = input("Type 'yes' to confirm deletion: ").lower().strip()
            
            if confirmation != 'yes':
                print("Deck deletion cancelled.")
                return False
            
            # Remove the file
            os.remove(file_path)
            print(f"Deck '{deck.name}' deleted successfully!")
            return True
            
        except Exception as e:
            print(f"Error deleting deck '{deck.name}': {e}")
            return False

    def add_flashcard(self, deck, flashcard):
        deck.add_flashcard(flashcard)
        self.save_deck(deck)

    def remove_flashcard(self, deck, flashcard):
        deck.remove_flashcard(flashcard)
        self.save_deck(deck)

    def list_decks(self):
        if not os.path.exists(self.decks_folder):
            print("Deck folder not found")
            return []
        
        # Add decks to list
        deck_files = []
        for file in os.listdir(self.decks_folder): # current directory
            if file.endswith('.json'):
                deck_files.append(file) # add deck name to list
        return deck_files

        # if no decks found, return empty list
        if not deck_files:
            print("No decks found")
            return []
        
        # Load decks from files
        deck_names = []
        for deck_file in deck_files:
            deck_name = deck_file[:-5]  # Remove .json extension
            deck_names.append(deck_name)
        return deck_names
    