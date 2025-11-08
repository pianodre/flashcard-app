// Used to store lists of flashcards

import java.util.List;
import java.util.ArrayList;

public class FlashcardSet {
    List<Flashcard> flashcards; // List of flashcards in the set

    // Constructor
    public FlashcardSet() {
        this.flashcards = new ArrayList<>(); // Initialize the list
    }

    // Add a flashcard to the set
    public void addFlashcard(Flashcard flashcard) {
        this.flashcards.add(flashcard);
    }
    
    // Remove a flashcard from the set
    public void removeFlashcard(Flashcard flashcard) {
        this.flashcards.remove(flashcard);
    }

    // Get the list of flashcards in the set
    public List<Flashcard> getFlashcards() {
        return this.flashcards;
    }

    

    // Custom toString to print flashcards one by one
    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();
        for (Flashcard flashcard : flashcards) {
            result.append(flashcard.toString() + "\n");
        }
        return result.toString();
    }
}
