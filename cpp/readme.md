# Flashcard App (C++)

A console-based flashcard application for studying and memorization.

## Current Features

- **Flashcard Class**: Basic flashcard with front/back content and difficulty rating
- **Deck Class**: Collection management for flashcards with file I/O
- **Study Session**: Interactive console-based study loop with difficulty rating
- **File Persistence**: Save/load decks from text files

## TODO: Study System Development

### Phase 1: Basic Flashcard Model ✅

- [X] Implement `Flashcard` class with:
  - [X] `front` and `back` content
  - [X] `difficulty` rating (1-3 scale)
- [X] Add corresponding getters/setters
- [X] Basic constructor implementation

### Phase 2: Study Session Core ✅

- [X] Create `StudySession` class with:
  - [X] Session initialization with a deck
  - [X] Current card tracking
  - [X] Difficulty rating interface
  - [X] Basic console-based study loop
- [X] Implement session state management
- [X] Add basic session summary

### Phase 3: File Persistence ✅

- [X] Implement file I/O capabilities:
  - [X] Save/load decks to/from files
  - [X] Simple text-based format (front, back, difficulty)
- [X] Data validation for loaded files
- [ ] Backup/restore functionality

### Phase 4: Enhanced Study Features 🚀

- [ ] Add study mode selection:
  - [ ] Review mode (difficult cards only)
  - [ ] All cards mode
  - [ ] Random vs. ordered study
- [ ] Improve user experience:
  - [ ] Better input validation
  - [ ] Progress indicators during session
  - [ ] Enhanced session summaries
- [ ] Multiple study approaches:
  - [ ] Traditional flashcard review
  - [ ] Multiple choice mode
  - [ ] Typing practice mode

### Phase 5: Polish & Optimization ✨

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
g++ -o flashcard_app main.cpp Flashcard.cpp Deck.cpp StudySession.cpp
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
├── StudySession.h    # Study session class header
├── StudySession.cpp  # Study session class implementation
├── decks/           # Directory containing deck files
└── README.md        # This file
```

## Future Considerations

- GUI implementation (after console version is complete)
- Database integration for larger datasets
- Multi-user support
- Cloud synchronization
- Mobile app version
