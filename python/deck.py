import random
from datetime import datetime

class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.current_index = 0
        self.created_date = datetime.now().isoformat()
        self.last_studied = self.created_date

    def add_flashcard(self, card):
        self.cards.append(card)

    def remove_flashcard(self, card):
        self.cards.remove(card)

    def shuffle_within_difficulty(self):
        # Sort by difficulty
        self.cards.sort(key=lambda c: c.difficulty)
        start = 0
        while start < len(self.cards):
            diff = self.cards[start].difficulty
            end = start
            while end < len(self.cards) and self.cards[end].difficulty == diff:
                end += 1
            random.shuffle(self.cards[start:end])
            start = end

    def getDeckLength(self):
        return len(self.cards)

    def getCurrentIndex(self):
        return self.current_index
    
    def next_card(self):
        if self.current_index < len(self.cards) - 1:
            self.current_index += 1
        return self.current_index
    
    def reset_index(self):
        self.current_index = 0