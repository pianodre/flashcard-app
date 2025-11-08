public class Flashcard {
    String front;
    String back;

    public Flashcard() {
        this.front = "";
        this.back = "";
    }
    
    public Flashcard(String front, String back) {
        this.front = front;
        this.back = back;
    }

    // Getters 
    public String getFront() {
        return front;
    }

    public String getBack() {
        return back;
    }

    // Setters
    public void setFront(String front) {
        this.front = front;
    }

    public void setBack(String back) {
        this.back = back;
    }

    // toString method for better printing
    @Override
    public String toString() {
        return "Front: " + front + " | Back: " + back;
    }

}
