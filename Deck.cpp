#include "Deck.h"

Deck::Deck() { // Constructor
    deckName = "";
    cards = vector<Flashcard>();
} 

Deck::Deck(string name) {
    deckName = name;
    cards = vector<Flashcard>();
}

Deck::~Deck() {} // Destructor

// Getters and Setters
string Deck::getDeckName() {
    return deckName;
}
void Deck::setDeckName(string name) {
    deckName = name;
}

// Additional Functions
void Deck::addFlashcard(const Flashcard& card) {
    cards.push_back(card);
}

vector<Flashcard> Deck::getFlashcards() {
    return cards;
}
Flashcard Deck::getFlashcardAt(int index) {
    return cards[index];
}
int Deck::getFlashcardCount() {
    return cards.size();
}

void Deck::shuffleDeck() {
    random_device rd;
    mt19937 g(rd());
    shuffle(cards.begin(), cards.end(), g);
}

void Deck::printDeck() {
    for (int i = 0; i < cards.size(); i++) {
        cout << cards[i].getFront() << endl;
    }
}