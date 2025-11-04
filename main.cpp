#include "Flashcard.h"
#include "Deck.h"
#include "StudySession.h"

int main (int argc, char **argv) {
    // Create object
    Flashcard flashcard1("Front 1", "Back 1"); // Stack allocation using default constructor
    Flashcard flashcard2("Front 2", "Back 2"); // Stack allocation using default constructor
    Flashcard flashcard3("Front 3", "Back 3"); // Stack allocation using default constructor
    Flashcard flashcard4("Front 4", "Back 4"); // Stack allocation using default constructor
    

    Deck deck1("Deck 1");

    deck1.addFlashcard(flashcard1);
    deck1.addFlashcard(flashcard2);
    deck1.addFlashcard(flashcard3);
    deck1.addFlashcard(flashcard4);
    deck1.shuffleDeck();

    cout << "\n" << endl;

    StudySession session(deck1);
    session.startSession();

    return 0;
}