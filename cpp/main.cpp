#include "Flashcard.h"
#include "Deck.h"
#include "StudySession.h"

int main (int argc, char **argv) {

    cout << "Which deck would you like to study? " << endl;
    Deck::listAvailableDecks("./decks");
    string deckName;
    cin >> deckName;
    cout << "\n" << endl;

    // Create deck and load from file
    Deck deck1(deckName);
    string filepath = "./decks/" + deckName + ".txt";
    deck1.loadFromFile(filepath);
    
    StudySession session(deck1);
    session.startSession();
    
    // Save updated difficulty ratings back to file
    deck1.saveDeck(filepath);

    return 0;
}