# Flashcard App - TODO List

## 🔧 High Priority - Fix Current Issues

### 1. Fix StudySession Logic Issues

- [X] **Fix card modification problem**: Currently modifying a copy of the card, not the original in deck
- [X] **Implement reference-based card updates**: Use references or pointers to modify cards in the deck directly
- [X] **Connect difficulty rating to learning progress**: Make difficulty ratings actually affect the card's stored data

## 📝 Medium Priority - Core Features

### 3. Add File Persistence (Phase 4 from README)

- [ ] **Save decks to files**: Implement file output for deck data
- [X] **Load decks from files**: Read deck data back from saved files
- [ ] **Persist study statistics**: Save card progress (difficulty, times correct/incorrect, etc.)
- [ ] **Simple text-based format**: Use CSV or simple text format initially
- [ ] **Data validation**: Validate loaded file data for corruption/errors
- [ ] **Backup/restore functionality**: Prevent data loss

### 4. Enhance Study Modes

- [ ] **Review mode**: Study only difficult cards (difficulty 4-5)
- [ ] **New cards mode**: Study cards that haven't been reviewed yet
- [ ] **Mixed mode**: Combine new and review cards intelligently
- [ ] **Study mode selection**: Let user choose which mode to use

## 🎯 Lower Priority - Advanced Features

### 5. Implement Basic Spaced Repetition

- [ ] **Add timestamp tracking**: Track `lastReviewed` and `nextReview` dates
- [ ] **Interval calculation**: Calculate review intervals based on performance
- [ ] **Priority queue**: Order cards by due date for review
- [ ] **Mastery levels**: Track when cards are "mastered" (consistently correct)

### 6. Improve User Experience

- [ ] **Better input validation**: Handle invalid inputs gracefully
- [ ] **Clear screen functionality**: Make interface cleaner between cards
- [ ] **Progress indicators**: Show "Card X of Y" during sessions
- [ ] **Session summaries**: More detailed statistics at end of session

### 7. Code Quality & Polish

- [ ] **Error handling**: Add try-catch blocks and input validation
- [ ] **Code documentation**: Add comments explaining complex logic
- [ ] **Memory management**: Ensure no memory leaks
- [ ] **Unit tests**: Create test cases for core functionality

## 🚀 Future Enhancements

### 8. Advanced Study Features

- [ ] **Multiple choice mode**: Generate wrong answers automatically
- [ ] **Typing practice mode**: User types the answer instead of self-assessment
- [ ] **Hint system**: Provide hints for difficult cards
- [ ] **Card categories/tags**: Organize cards by subject or difficulty

### 9. Data & Analytics

- [ ] **Study streaks**: Track daily study habits
- [ ] **Performance analytics**: Charts showing improvement over time
- [ ] **Export statistics**: Generate study reports
- [ ] **Multiple decks**: Support for multiple deck files

## 📋 Immediate Next Steps

**Start Here:**

1. Fix the StudySession card modification issue (Item #1)
2. Add proper correct/incorrect tracking (Item #2)
3. Test with real study session to verify fixes work

**Recommended Order:**

1. High Priority items (1-2)
2. File Persistence (3) - makes app actually useful
3. Study Modes (4) - improves learning effectiveness
4. Everything else based on user needs

---

*Last Updated: November 4, 2025*
