from deck import Deck
from flashcard import Flashcard
from deckManager import DeckManager

def test_deck_manager():
    """Test all DeckManager functions with a new test deck"""
    print("=== Testing DeckManager Functions ===\n")
    
    # Initialize DeckManager
    deck_manager = DeckManager()
    
    # Test 1: Create a new test deck
    print("1. Creating a new test deck...")
    test_deck = Deck("Python Basics")
    
    # Add sample flashcards to the test deck
    sample_cards = [
        Flashcard("What is a variable in Python?", "A variable is a name that refers to a value stored in memory", 1),
        Flashcard("What does 'len()' function do?", "Returns the number of items in an object", 2),
        Flashcard("How do you create a list in Python?", "Use square brackets: my_list = [1, 2, 3]", 1),
        Flashcard("What is the difference between '==' and 'is'?", "'==' compares values, 'is' compares object identity", 3),
        Flashcard("How do you handle exceptions in Python?", "Use try/except blocks", 2)
    ]
    
    for card in sample_cards:
        test_deck.add_flashcard(card)
    
    print(f"   ✓ Created test deck with {len(test_deck.cards)} cards")
    
    # Test 2: Test create_deck() function
    print("\n2. Testing create_deck() function...")
    deck_manager.create_deck(test_deck)
    print("   ✓ create_deck() completed")
    
    # Test 3: Test list_decks() function
    print("\n3. Testing list_decks() function...")
    all_decks = deck_manager.list_decks()
    print(f"   ✓ Found {len(all_decks)} decks:")
    for deck_name in all_decks:
        print(f"     - {deck_name}")
    
    # Test 4: Test load_deck() function
    print("\n4. Testing load_deck() function...")
    loaded_deck = deck_manager.load_deck("python_basics")
    if loaded_deck:
        print(f"   ✓ Successfully loaded deck: '{loaded_deck.name}' with {len(loaded_deck.cards)} cards")
        
        # Display first card as example
        if loaded_deck.cards:
            first_card = loaded_deck.cards[0]
            print(f"     Example card: {first_card.get_question()}")
            print(f"     Answer: {first_card.get_answer()}")
    else:
        print("   ✗ Failed to load deck")
    
    # Test 5: Test add_flashcard() function
    print("\n5. Testing add_flashcard() function...")
    new_card = Flashcard("What is a dictionary in Python?", "A collection of key-value pairs enclosed in curly braces", 1)
    deck_manager.add_flashcard(loaded_deck, new_card)
    print(f"   ✓ Added new flashcard. Deck now has {len(loaded_deck.cards)} cards")
    
    # Test 6: Test save_deck() function
    print("\n6. Testing save_deck() function...")
    result = deck_manager.save_deck(loaded_deck)
    if result:
        print("   ✓ Deck saved successfully")
    else:
        print("   ✗ Failed to save deck")
    
    # Test 7: Test remove_flashcard() function
    print("\n7. Testing remove_flashcard() function...")
    if loaded_deck.cards:
        card_to_remove = loaded_deck.cards[-1]  # Remove the last card
        original_count = len(loaded_deck.cards)
        deck_manager.remove_flashcard(loaded_deck, card_to_remove)
        print(f"   ✓ Removed flashcard. Deck now has {len(loaded_deck.cards)} cards (was {original_count})")
    
    # Test 8: Display final deck state
    print("\n8. Final deck state:")
    final_deck = deck_manager.load_deck("python_basics")
    if final_deck:
        print(f"   Deck: '{final_deck.name}'")
        print(f"   Cards: {len(final_deck.cards)}")
        print("   Card list:")
        for i, card in enumerate(final_deck.cards, 1):
            print(f"     {i}. Q: {card.get_question()}")
            print(f"        A: {card.get_answer()}")
            print(f"        Difficulty: {card.get_difficulty()}")
    
    # Test 9: Test remove_deck() function (optional - commented out for safety)
    print("\n9. Testing remove_deck() function...")
    print("   Note: remove_deck() test is available but commented out for safety.")
    print("   Uncomment the lines below if you want to test deck deletion:")
    print("   # deck_manager.remove_deck(final_deck)")
    
    # Uncomment the line below to test deck removal (will ask for confirmation)
    # deck_manager.remove_deck(final_deck)
    
    print("\n=== All DeckManager Tests Completed ===")

def testDeck():
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
    
    print(f"\n=== Testing Deck: {current_deck.name} ===")
    print(f"Total cards: {len(current_deck.cards)}\n")
    
    # Loop through each flashcard
    for i, card in enumerate(current_deck.cards, 1):
        print(f"Card {i}/{len(current_deck.cards)}")
        print("-" * 40)
        print(f"Question: {card.get_question()}")
        print(f"Current Difficulty: {card.get_difficulty()}")
        
        input("\nPress Enter to see the answer...")
        print(f"Answer: {card.get_answer()}")
        
        # Prompt for difficulty change
        print("\nDifficulty levels:")
        print("1 - Easy")
        print("2 - Medium") 
        print("3 - Hard")
        
        while True:
            new_difficulty = input(f"Enter new difficulty (1-3) or press Enter to keep current ({card.get_difficulty()}): ").strip()
            
            if new_difficulty == "":
                # Keep current difficulty
                break
            elif new_difficulty in ["1", "2", "3"]:
                old_difficulty = card.get_difficulty()
                card.edit_flashcard(card.get_question(), card.get_answer(), int(new_difficulty))
                print(f"Difficulty changed from {old_difficulty} to {new_difficulty}")
                break
            else:
                print("Please enter 1, 2, 3, or press Enter to keep current difficulty.")
        
        print("\n" + "="*50 + "\n")
    
    # Save the deck with any changes
    deck_manager.save_deck(current_deck)
    print(f"\nDeck '{current_deck.name}' has been saved with any changes!")

def main():
    """Run the DeckManager tests"""
    # test_deck_manager()
    testDeck()

if __name__ == "__main__":
    main()
