#ifndef DECK_H
#define DECK_H

#include <iostream>
#include <vector>
#include "Flashcard.h"
#include <algorithm>
#include <random>
#include <string>
#include <dirent.h>
#include <fstream>
#include <sstream>

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
        Flashcard& getFlashcardAt(int index);
        int getFlashcardCount();
        void shuffleDeck();
        void sortByDifficulty();  // Sort cards by difficulty (hardest first)
        void shuffleWithinDifficulty();  // Shuffle cards within each difficulty group
        void printDeck();
        static void listAvailableDecks(const string& folderPath);
        void loadFromFile(const string& filename);
        void saveDeck(const string& filename);

    private:
        string deckName;
        vector<Flashcard> cards;

};


#endif