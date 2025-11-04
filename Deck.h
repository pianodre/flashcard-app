#ifndef DECK_H
#define DECK_H

#include <iostream>
#include <vector>
#include "Flashcard.h"
#include <algorithm>
#include <random>

using namespace std;

class Deck {

    public:
        Deck(); // Constructor
        Deck(string name); // Parameterized constructor
        ~Deck(); // Destructor

        string getDeckName();
        void setDeckName(string name);

        void addFlashcard(const Flashcard& card); // & reference the original dont copy it
        vector<Flashcard> getFlashcards();
        Flashcard getFlashcardAt(int index);
        int getFlashcardCount();
        void shuffleDeck();
        void printDeck();

    private:
        string deckName;
        vector<Flashcard> cards;

};


#endif