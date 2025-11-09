from datetime import datetime, timedelta

class Flashcard:
    def __init__(self, question, answer, difficulty, times_studied=0, last_review=None):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty
        self.times_studied = times_studied
        self.last_review = last_review
        self.next_review = None

    def to_dict(self): # turns card into a dictionary in order to load/save it
        return {
            "question": self.question,
            "answer": self.answer,
            "difficulty": self.difficulty,
            "times_studied": self.times_studied,
            "last_review": self.last_review,
            "next_review": self.next_review
        }

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_difficulty(self):
        return self.difficulty

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
    
    def edit_flashcard(self, question, answer, difficulty):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty
        self.last_review = datetime.now().isoformat()
        self.times_studied += 1
        self.next_review = self._calculate_next_review(difficulty)
        
    def _calculate_next_review(self, difficulty):
        """Calculate next review date based on difficulty"""
        now = datetime.now()

        if difficulty == 1:  # Easy
            # Get tomorrow's date
            next_day = now + timedelta(days=1)
            # Set time to exactly midnight (00:00:00.000)
            next_time = next_day.replace(hour=0, minute=0, second=0, microsecond=0)
        elif difficulty == 2:  # Medium
            next_time = now + timedelta(minutes=5)
        elif difficulty == 3:  # Hard
            next_time = now + timedelta(seconds=30)

        return next_time.isoformat()
            
    def is_due_for_review(self):
        """Check if the card is due for review"""
        if not self.next_review:
            return True
        
        now = datetime.now()
        next_review_time = datetime.fromisoformat(self.next_review)
        return now >= next_review_time

