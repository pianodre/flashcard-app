import os
from deck import Deck
from flashcard import Flashcard
from deckManager import DeckManager

class IOControl:
    def __init__(self):
        self.deck_manager = DeckManager()
    
    def import_txt_file(self):
        """Import flashcards from a text file and create a new deck"""
        
        # Get deck name from user
        deck_name = input("Enter the name for your new deck: ").strip()
        if not deck_name:
            print("Deck name cannot be empty!")
            return False
        
        # Get file path from user
        file_path = input("Enter the path to your .txt file: ").strip()
        
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"File '{file_path}' not found!")
            return False
        
        # Check if it's a .txt file
        if not file_path.lower().endswith('.txt'):
            print("Please provide a .txt file!")
            return False
        
        try:
            # Read and parse the file
            cards = self._parse_txt_file(file_path)
            
            if not cards:
                print("No valid cards found in the file!")
                return False
            
            # Create new deck
            new_deck = Deck(deck_name)
            
            # Add all cards to the deck
            for card in cards:
                new_deck.add_flashcard(card)
            
            # Save the deck using DeckManager
            success = self.deck_manager.create_deck(new_deck)
            
            if success:
                print(f"\n✅ Successfully imported {len(cards)} cards!")
                print(f"✅ Deck '{deck_name}' created and saved as JSON file!")
                return True
            else:
                print("❌ Failed to save the deck!")
                return False
                
        except Exception as e:
            print(f"❌ Error importing file: {e}")
            return False
    
    def _parse_txt_file(self, file_path):
        """Parse the text file and return a list of Flashcard objects"""
        cards = []
        
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Split by comma
            parts = [part.strip() for part in line.split(',')]
            
            # Validate format
            if len(parts) < 2:
                print(f"⚠️  Warning: Line {line_num} skipped - needs at least Front and Back: '{line}'")
                continue
            elif len(parts) > 3:
                print(f"⚠️  Warning: Line {line_num} has too many parts, using first 3: '{line}'")
                parts = parts[:3]
            
            # Extract components
            front = parts[0]
            back = parts[1]
            
            # Handle difficulty
            if len(parts) == 3:
                try:
                    difficulty = int(parts[2])
                    # Validate difficulty range
                    if difficulty not in [1, 2, 3]:
                        print(f"⚠️  Warning: Line {line_num} - difficulty must be 1, 2, or 3. Using default (1): '{line}'")
                        difficulty = 1
                except ValueError:
                    print(f"⚠️  Warning: Line {line_num} - invalid difficulty '{parts[2]}'. Using default (1): '{line}'")
                    difficulty = 1
            else:
                difficulty = 1  # Default difficulty
            
            # Validate front and back are not empty
            if not front or not back:
                print(f"⚠️  Warning: Line {line_num} skipped - Front and Back cannot be empty: '{line}'")
                continue
            
            # Create flashcard
            card = Flashcard(front, back, difficulty)
            cards.append(card)
            
        return cards
    
    def export_deck_to_txt(self):
        """Export a deck to a text file in the same format as import"""
        
        # Get list of available decks
        deck_names = self.deck_manager.list_decks()
        
        if not deck_names:
            print("No decks found to export!")
            return False
        
        # Display available decks
        print("Available decks to export:")
        for i, deck_name in enumerate(deck_names, 1):
            clean_name = deck_name.replace('.json', '').replace('_', ' ').title()
            print(f"{i}. {clean_name}")
        
        # Get user's deck selection
        try:
            choice = int(input("\nSelect a deck number to export: ")) - 1
            if choice < 0 or choice >= len(deck_names):
                print("Invalid selection!")
                return False
            
            selected_deck_file = deck_names[choice]
            selected_deck_name = selected_deck_file.replace('.json', '')
            
        except ValueError:
            print("Please enter a valid number!")
            return False
        
        # Load the selected deck
        deck = self.deck_manager.load_deck(selected_deck_name)
        if not deck:
            print("Failed to load deck!")
            return False
        
        # Get export directory
        export_dir = input("Enter the directory path where you want to save the file: ").strip()
        
        # Validate directory exists
        if not os.path.exists(export_dir):
            print(f"Directory '{export_dir}' does not exist!")
            return False
        
        if not os.path.isdir(export_dir):
            print(f"'{export_dir}' is not a directory!")
            return False
        
        try:
            # Create filename
            safe_deck_name = deck.name.lower().replace(" ", "_").replace("-", "_")
            filename = f"{safe_deck_name}.txt"
            file_path = os.path.join(export_dir, filename)
            
            # Write cards to file
            with open(file_path, 'w', encoding='utf-8') as file:
                for card in deck.cards:
                    front = card.get_question()
                    back = card.get_answer()
                    difficulty = card.get_difficulty()
                    
                    # Check if difficulty is null/None or empty
                    if difficulty is None or difficulty == "":
                        # Export without difficulty
                        line = f"{front}, {back}\n"
                    else:
                        # Export with difficulty
                        line = f"{front}, {back}, {difficulty}\n"
                    
                    file.write(line)
            
            print(f"\n✅ Successfully exported {len(deck.cards)} cards!")
            print(f"✅ File saved as: {file_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error exporting deck: {e}")
            return False

