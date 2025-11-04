#ifndef STUDYSESSION_H
#define STUDYSESSION_H

#include "Deck.h"
#include "Flashcard.h"
#include <algorithm>
#include <random>

class StudySession {
    public:
        StudySession(Deck deck);
        ~StudySession();
        void startSession();
        void displayFront();
        void displayBack();
        void shuffleDeck();
        

    private:
        Deck deck;
        Flashcard currentCard;
};


#endif