#include "StudySession.h"

StudySession::StudySession(Deck& deck) : deck(deck) {
}

StudySession::~StudySession() {}

void StudySession::startSession() {
    if (deck.getFlashcardCount() == 0) {
        cout << "No cards in deck to study." << endl;
        return;
    }

    deck.shuffleWithinDifficulty();  // Shuffle within each difficulty group

    cout << "Starting study session for " << deck.getFlashcardCount() << " cards." << endl;
    cout << "Deck: " << deck.getDeckName() << endl;
    cout << "Press Enter to begin...." << endl;
    cin.ignore(); // Waits for user input

    // Initialize Session Variables
    int currentIndex = 0;
    int correctCount = 0;
    int totalStudied = 0;

    // Main Study Loop
    while (true) {
        if (currentIndex >= deck.getFlashcardCount()) {
            currentIndex = 0;
            deck.shuffleWithinDifficulty();  // Shuffle within each difficulty group
        }
        
        Flashcard& currentCardRef = deck.getFlashcardAt(currentIndex);

        cout << "\nFront: " << currentCardRef.getFront() << " : " << currentCardRef.getDifficulty() << endl;
        cout << "Press Enter to reveal back..." << endl;
        cin.ignore(); // Waits for user input

        cout << "\nBack: " << currentCardRef.getBack() << endl;

        cout << "Enter '1-3' to rate difficulty or 'exit' to quit: ";
        string response;
        cin >> response;
        cin.ignore(); // Waits for user input

        if (response == "exit") {
            cout << "Exiting study session..." << endl;
            break;
        } else if (response == "1") {
            currentCardRef.setDifficulty(1);
        } else if (response == "2") {
            currentCardRef.setDifficulty(2);
        } else if (response == "3") {
            currentCardRef.setDifficulty(3);
        }
        
        totalStudied++;
        currentIndex++;
        
    }
    
    cout << "Total Studied: " << totalStudied << endl;
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
