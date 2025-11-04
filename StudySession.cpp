#include "StudySession.h"

StudySession::StudySession(Deck deck) {
    this->deck = deck;
}

StudySession::~StudySession() {}

void StudySession::startSession() {
    if (deck.getFlashcardCount() == 0) {
        cout << "No cards in deck to study." << endl;
        return;
    }

    cout << "Starting study session for " << deck.getFlashcardCount() << " cards." << endl;
    cout << "Deck: " << deck.getDeckName() << endl;
    cout << "Press Enter to begin...." << endl;
    cin.ignore(); // Waits for user input

    // Initialize Session Variables
    int currentIndex = 0;
    int correctCount = 0;
    int totalStudied = 0;

    // Main Study Loop
    while (currentIndex < deck.getFlashcardCount()) {
        currentCard = deck.getFlashcardAt(currentIndex);

        cout << "\nFront: " << currentCard.getFront() << endl;
        cout << "Press Enter to reveal back..." << endl;
        cin.ignore(); // Waits for user input

        cout << "\nBack: " << currentCard.getBack() << endl;

        cout << "Enter '1-5' to rate difficulty: ";
        char response;
        cin >> response;
        cin.ignore(); // Waits for user input

        if (response == '1') {
            currentCard.setDifficulty(1);
        } else if (response == '2') {
            currentCard.setDifficulty(2);
        } else if (response == '3') {
            currentCard.setDifficulty(3);
        } else if (response == '4') {
            currentCard.setDifficulty(4);
        } else if (response == '5') {
            currentCard.setDifficulty(5);
        }
        
        totalStudied++;
        currentIndex++;
    }
    
    cout << "Total Studied: " << totalStudied << endl;
    cout << "Correct: " << correctCount << endl;
    cout << "Incorrect: " << totalStudied - correctCount << endl;
    cout << "Press Enter to return to main menu..." << endl;
    cin.ignore(); // Waits for user input

}

void StudySession::displayFront() {
    cout << deck.getFlashcardAt(0).getFront() << endl;
}

void StudySession::displayBack() {
    cout << deck.getFlashcardAt(0).getBack() << endl;
}

void StudySession::shuffleDeck() {
    deck.shuffleDeck();
}
