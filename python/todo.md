# Flashcard App TODO - November 9, 2025 🎯

## 🚀 PRIORITY: Infinite Study Mode Implementation

### **Main Goal: Enable Continuous Study Sessions**

Implement a system that allows users to study a deck infinitely by showing cards even when their `next_review` time hasn't passed yet.

### **Core Requirements:**

1. **Smart Card Selection Logic** 📚
   - **Primary**: Show cards that are actually due (normal spaced repetition)
   - **Secondary**: When no cards are due, show cards by difficulty priority:
     - First: All cards marked as **Hard (difficulty 3)**
     - Then: All cards marked as **Medium (difficulty 2)**
     - Last: Cards marked as **Easy (difficulty 1)** only if no Hard/Medium exist

2. **Utilize Existing Shuffle Function** 🔀
   - Use the existing `shuffle_within_difficulty()` function in `deck.py`
   - This ensures cards of the same difficulty are randomized
   - Maintains variety within difficulty groups

### **Implementation Tasks:**

#### **Backend Changes (Python):**
- [ ] **Modify `get_due_cards()` method in `deck.py`**
  - Add fallback logic when no cards are actually due
  - Implement priority system: Hard → Medium → Easy
  - Integrate with `shuffle_within_difficulty()` for randomization

- [ ] **Update API endpoint `/api/study/<deck_name>`**
  - Modify to use new infinite study logic
  - Ensure it returns cards even when none are "due"
  - Add metadata to indicate if cards are "due" vs "practice"

#### **Frontend Changes (JavaScript):**
- [ ] **Update study session UI**
  - Add visual indicator when studying "practice" cards vs "due" cards
  - Show different messaging: "No cards due - practicing Hard cards" etc.
  - Maintain existing difficulty rating functionality

#### **User Experience Enhancements:**
- [ ] **Visual Feedback**
  - Different card border colors for due vs practice cards
  - Status message showing current study mode
  - Progress indicator that accounts for infinite study

- [ ] **Study Session Options**
  - Allow users to choose: "Due cards only" vs "Infinite study"
  - Add "Stop studying" button for infinite sessions
  - Show statistics: "X due cards completed, now practicing"

### **Technical Implementation Notes:**

#### **Priority Logic:**
```python
# Pseudocode for new get_study_cards() method:
1. Get actually due cards (existing logic)
2. If due_cards.length > 0: return due_cards
3. Else:
   - Get all Hard cards (difficulty 3)
   - If hard_cards.length > 0: shuffle and return hard_cards
   - Else get all Medium cards (difficulty 2)
   - If medium_cards.length > 0: shuffle and return medium_cards
   - Else get all Easy cards (difficulty 1) as last resort
```

#### **Files to Modify:**
- `src/deck.py` - Update card selection logic
- `app/routes.py` - Modify study endpoint
- `app/static/js/flashcard.js` - Update UI for infinite mode
- `app/templates/flashcard.html` - Add visual indicators

### **Success Criteria:**
- ✅ Users can always study a deck (never see "no cards available")
- ✅ Spaced repetition still works normally for due cards
- ✅ Hard cards get priority practice when no cards are due
- ✅ Visual feedback clearly shows study mode (due vs practice)
- ✅ Existing functionality remains unchanged

---

## 🎯 Current Status (Nov 8, 2025 - COMPLETED)

### ✅ **Major Accomplishments - Web App Complete!**

- **Flask Web Application** - Fully functional with all features
- **Spaced Repetition System** - Working with proper difficulty mapping
- **Interactive Frontend** - Card flipping, difficulty buttons, real-time updates
- **API Integration** - Complete CRUD operations for decks and cards
- **Proper Time Management** - Easy cards now due at midnight next day
- **Fixed Difficulty Mapping** - 1=Easy(1day), 2=Medium(5min), 3=Hard(30sec)

### 🎉 **Ready for Tomorrow's Focus: Infinite Study Mode**

The foundation is solid - now we enhance the study experience to be more engaging and continuous!
