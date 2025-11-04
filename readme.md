# Flashcard App (C++)

A console-based flashcard application for studying and memorization.

## Current Features

- **Flashcard Class**: Basic flashcard with front/back content
- **Deck Class**: Collection management for flashcards
- **Basic Operations**: Create, store, and access flashcards

## TODO: Study System Development

### Phase 1: Enhanced Flashcard Model ⏳

- [X] Extend `Flashcard` class with study-related properties:
  - [X] `difficulty` (1-5 scale)
  - [X] `lastReviewed` (timestamp)
  - [X] `nextReview` (timestamp)
  - [X] `timesCorrect` / `timesIncorrect` counters
  - [X] `consecutiveCorrect` streak
- [X] Add corresponding getters/setters
- [X] Update constructors to handle new properties

### Phase 2: Study Session Core 📚

- [X] Create `StudySession` class with:
  - [X] Session initialization with a deck
  - [X] Current card tracking
  - [X] Answer validation methods
  - [X] Session statistics collection
  - [X] Basic console-based study loop
- [X] Implement session state management
- [X] Add session summary/results display

### Phase 3: Basic Study Loop 🔄

- [X] Implement console-based study interface:
  - [X] Show front of card, wait for user input
  - [X] Reveal back, ask for self-assessment (correct/incorrect)
  - [X] Update card statistics based on performance
  - [ ] Move to next card with basic shuffling
- [ ] Add study mode selection (all cards, new cards, review)
- [ ] Implement card shuffling and randomization

### Phase 4: Persistence 💾

- [ ] Add file I/O capabilities:
  - [ ] Save/load decks to/from files
  - [ ] Persist study statistics and progress
  - [ ] Simple text-based format initially
- [ ] Implement data validation for loaded files
- [ ] Add backup/restore functionality

### Phase 5: Advanced Features 🚀

- [ ] Implement spaced repetition system:
  - [ ] Basic interval calculation based on performance
  - [ ] Priority queue for due cards
  - [ ] Different study modes (new cards, review, all)
- [ ] Add progress tracking and statistics:
  - [ ] `Statistics` class for long-term progress
  - [ ] Accuracy rates and streak counters
  - [ ] Mastery level tracking
- [ ] Multiple study approaches:
  - [ ] Traditional flashcard review
  - [ ] Multiple choice mode
  - [ ] Typing practice mode

### Phase 6: Polish & Optimization ✨

- [ ] Error handling and input validation
- [ ] Performance optimization for large decks
- [ ] Code documentation and comments
- [ ] Unit testing framework
- [ ] Memory management optimization

## Getting Started

### Prerequisites

- C++ compiler (g++, clang++, etc.)
- Standard C++ library

### Building

```bash
g++ -o flashcard_app main.cpp Flashcard.cpp Deck.cpp
```

### Running

```bash
./flashcard_app
```

## Project Structure

```
cpp/
├── main.cpp          # Main application entry point
├── Flashcard.h       # Flashcard class header
├── Flashcard.cpp     # Flashcard class implementation
├── Deck.h           # Deck class header
├── Deck.cpp         # Deck class implementation
└── README.md        # This file
```

## Future Considerations

- GUI implementation (after console version is complete)
- Database integration for larger datasets
- Multi-user support
- Cloud synchronization
- Mobile app version
