from datetime import datetime

class Flashcard:
    def __init__(self, question, answer, difficulty, times_studied=0, last_review=None):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty
        self.times_studied = times_studied
        self.last_review = last_review

    def to_dict(self): # turns card into a dictionary in order to load/save it
        return {
            "question": self.question,
            "answer": self.answer,
            "difficulty": self.difficulty,
            "times_studied": self.times_studied,
            "last_review": self.last_review
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
        
