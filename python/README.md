# Revu Flashcard App

A spaced repetition flashcard application built in Python, designed to help with learning and memorization through intelligent review scheduling.

## Current Features

- **Flashcard Management**: Create flashcards with questions, answers, and difficulty levels
- **Deck Organization**: Group flashcards into named decks
- **Smart Shuffling**: Shuffle cards within difficulty levels to maintain learning progression
- **Console Interface**: Simple text-based interaction for studying

## Project Structure

```
python/
├── main.py              # Main application entry point
├── Flashcard.py         # Flashcard class definition
├── Deck.py             # Deck class for managing collections of flashcards
├── FlashcardTesting.py # Testing framework for flashcard functionality
└── README.md           # This file
```

## Current Implementation

### Classes

- **`flashcard`**: Represents individual flashcards with question, answer, and difficulty
- **`deck`**: Manages collections of flashcards with shuffling capabilities
- **`flashcardTesting`**: Provides testing framework for deck functionality

### Usage Example

```python
from deck import Deck
from flashcard import Flashcard

# Create a new deck
deck = Deck("Spanish Vocabulary")

# Add flashcards
deck.add_flashcard(Flashcard("Hola", "Hello", 1))
deck.add_flashcard(Flashcard("Adiós", "Goodbye", 1))

# Shuffle within difficulty levels
deck.shuffle_within_difficulty()

# Study the cards
for card in deck.cards:
    input(f"Q: {card.question} ")
    print(f"A: {card.answer}")
```

## Running the Application

```bash
cd python
python main.py
```

## Future Vision

This console application is planned to evolve into a full-featured web application with:

- **Flask Web Framework**: Modern web interface
- **Spaced Repetition System**: Intelligent review scheduling based on performance
- **Interactive Buttons**:
  - 🔴 **Hard** (Red): Review again within 1 minute
  - 🔵 **Okay** (Blue): Review again within 10 minutes
  - 🟢 **Easy** (Green): Review next calendar day (resets at 12 AM)
- **Progress Tracking**: Monitor learning progress over time
- **Persistent Storage**: Save decks and progress between sessions

## Development Status

Currently in **console development phase**. The goal is to perfect the core functionality before transitioning to the web interface.

## Contributing

This is a personal learning project. The focus is on building a solid foundation in the console version before expanding to web technologies.

## License

Personal project - not currently licensed for distribution.
