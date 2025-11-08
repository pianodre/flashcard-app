public class app {
    public static void main(String[] args) {
        Flashcard flashcard1 = new Flashcard();
        flashcard1.setFront("What is the capital of France?");
        flashcard1.setBack("Paris");

        Flashcard flashcard2 = new Flashcard();
        flashcard2.setFront("What is the capital of Spain?");
        flashcard2.setBack("Madrid");

        FlashcardSet flashcardSet = new FlashcardSet();
        flashcardSet.addFlashcard(flashcard1);
        flashcardSet.addFlashcard(flashcard2);

        System.out.println(flashcardSet);
    }
}
