# Flashcard App Development Roadmap

## Phase 1: Console Version Completion 🎯

### Core Console Features

- [X] **User interaction improvements**

  - [X] Add difficulty rating after viewing each answer (1-3 scale)
  - [X] Add progress indicator (card X of Y)
- [X] **Enhanced deck management**

  - [X] Load decks from files (JSON)
  - [X] Save deck progress
  - [X] Multiple deck selection
  - [X] Deck statistics

### Data Persistence

- [X] **File-based storage**

  - [X] Save/load flashcard decks
  - [X] Track study history (difficulty changes, timestamps)
  - [X] Export/import functionality

## Phase 2: Spaced Repetition System 🧠

### Core Algorithm

- [X] **Implement spaced repetition logic** ✅ COMPLETED

  - [X] Add timestamp tracking to flashcards (already in edit_flashcard)
  - [X] Add next_review field to Flashcard class
  - [X] Implement review intervals based on difficulty:
    - Difficulty 1 (Hard) → 30 seconds (for testing)
    - Difficulty 2 (Medium) → 1 minute (for testing)
    - Difficulty 3 (Easy) → 5 minutes (for testing)
  - [X] Create scheduling algorithm in _calculate_next_review method
  - [X] Add is_due_for_review method to check if card should be shown

### Advanced Features

- [ ] **Smart scheduling**
  - [ ] Daily review limits
  - [ ] Priority queue for due cards
  - [ ] Overdue card handling
  - [ ] Review session optimization

## Phase 3: Web Application Migration 🌐

### Flask Setup

- [ ] **Project restructuring**

  - [ ] Create Flask application structure
  - [ ] Set up templates directory
  - [ ] Configure static files (CSS, JS)
  - [ ] Set up virtual environment
- [ ] **Backend development**

  - [ ] Convert classes to Flask models
  - [ ] Create API endpoints
  - [ ] Implement session management
  - [ ] Add database integration (SQLite → PostgreSQL)

### Frontend Development

- [ ] **UI/UX Design**

  - [ ] Design card interface mockups
  - [ ] Create responsive layout
  - [ ] Design button interactions (Hard/Okay/Easy)
  - [ ] Implement progress visualizations
- [ ] **Interactive Features**

  - [ ] Card flip animations
  - [ ] Button feedback (color coding)
  - [ ] Progress bars and statistics
  - [ ] Keyboard shortcuts

### Web-Specific Features

- [ ] **User Management**

  - [ ] User registration/login
  - [ ] Personal deck collections
  - [ ] Progress synchronization
  - [ ] Social features (deck sharing)
- [ ] **Advanced Web Features**

  - [ ] Mobile responsiveness
  - [ ] Offline capability (PWA)
  - [ ] Push notifications for reviews
  - [ ] Analytics dashboard

## Phase 4: Enhancement & Polish ✨

### Performance Optimization

- [ ] **Backend optimization**
  - [ ] Database query optimization
  - [ ] Caching implementation
  - [ ] API response optimization
  - [ ] Background task processing

### User Experience

- [ ] **Accessibility**

  - [ ] Screen reader support
  - [ ] Keyboard navigation
  - [ ] High contrast mode
  - [ ] Font size options
- [ ] **Customization**

  - [ ] Theme selection
  - [ ] Custom study intervals
  - [ ] Personalized difficulty algorithms
  - [ ] Custom card templates

### Testing & Quality

- [ ] **Comprehensive testing**
  - [ ] Unit tests for all classes
  - [ ] Integration tests
  - [ ] User acceptance testing
  - [ ] Performance testing

## Immediate Next Steps (This Week)

### DeckManager Implementation Priority Order ✅ COMPLETED

1. **✅ Implement create_deck(self, deck) function** - Create new decks
2. **✅ Implement save_deck(self, deck) function** - Persist decks to JSON files
3. **✅ Implement load_deck(self, deck_name) function** - Load existing decks from storage
4. **✅ Implement add_flashcard(self, deck, flashcard) function** - Add cards to decks
5. **✅ Implement remove_flashcard(self, deck, flashcard) function** - Remove cards from decks
6. **✅ Implement remove_deck(self, deck) function** - Delete entire decks

### Other Tasks

1. **✅ Fix current bugs in console version** - Fixed file loading issues
2. **✅ Implement basic user interaction flow** - Created testDeck() function for studying
3. **✅ Add file-based deck loading** - JSON loading/saving working perfectly
4. **✅ Create comprehensive test suite** - Full DeckManager testing implemented

## Current Status (Nov 8, 2025) 🎉

### ✅ Major Accomplishments Today

- **Complete DeckManager class** with all CRUD operations working
- **Interactive study function** (`testDeck()`) for going through flashcards
- **Difficulty editing system** allowing users to adjust card difficulty during study
- **Robust file handling** with JSON persistence and error handling
- **Comprehensive deck management** (create, edit, delete, view statistics)
- **Import/Export functionality** for .txt files with proper formatting
- **Working deck collection** with Spanish vocab, Math problems, and Python basics
- **✅ FIXED: Flashcard initialization bug** - Resolved issue where `next_review` was being passed as constructor parameter
- **✅ FIXED: UI display correction** - Changed "Next review" to "Last review" in study interface for better UX
- **🎉 MAJOR MILESTONE: Spaced Repetition System Complete!** - Full working spaced repetition with due card filtering and smart study options

### 🎯 Next Immediate Priorities

## **CURRENT FOCUS: Console Version Polish & Web Migration Prep**

### ✅ Spaced Repetition Implementation - COMPLETED!

1. **Update Flashcard class** (`flashcard.py`):

   - [X] ~~Add `next_review` parameter to `__init__` method~~ (next_review is set as instance variable)
   - [X] Import `timedelta` from datetime
   - [X] Add `next_review` field to `to_dict()` method
   - [X] Create `_calculate_next_review(difficulty)` method:
     - Difficulty 1 (Hard) → 30 seconds (for testing)
     - Difficulty 2 (Medium) → 5 minutes (for testing)
     - Difficulty 3 (Easy) → 1 day
   - [X] Add `is_due_for_review()` method
   - [X] Update `edit_flashcard()` to call `_calculate_next_review()`
2. **Update DeckManager class** (`deckManager.py`):

   - [X] ~~Add `next_review` parameter when loading flashcards in `load_deck()`~~ (Fixed: set as separate attribute)
3. **Update Deck class** (`deck.py`):

   - [X] Add `get_due_cards()` method to filter cards ready for review
   - [X] Add `get_cards_by_difficulty(difficulty)` method for filtering
4. **Update testDeck function** (`testFunctions.py`):

   - [X] Add option to study "All cards" vs "Due cards only"
   - [X] ~~Show next review time for each card~~ (Changed to "Last review" for better UX)
   - [X] Display how many cards are due vs total

### Other Enhancements (Lower Priority):

- [ ] Add session timer to track study time
- [ ] Add study session summary with statistics
- [ ] Implement "review only difficult cards" filter

## Long-term Goals

- **Robust spaced repetition algorithm** similar to Anki
- **Beautiful, intuitive web interface**
- **Mobile-first responsive design**
- **Community deck sharing**
- **Advanced analytics and progress tracking**

---

## Notes

- Focus on getting console version 100% working before web migration
- Prioritize core learning algorithm over fancy features
- Keep user experience simple and focused
- Plan for scalability in web version
