#include "Flashcard.h"

// Default Constructor
Flashcard::Flashcard(){}

// Overload Constructor
Flashcard::Flashcard(string front, string back) {
    this->front = front;
    this->back = back;
    difficulty = 1;
}

// Overload Constructor
Flashcard::Flashcard(string front, string back, int difficulty) {
    this->front = front;
    this->back = back;
    this->difficulty = difficulty;
}

// Deconstructor
Flashcard::~Flashcard(){}

// Setters
void Flashcard::setFront(string Front) {
    this->front = Front;
}
void Flashcard::setBack(string Back) {
    this->back = Back;
}
void Flashcard::setDifficulty(int difficulty) {
    this->difficulty = difficulty;
}

// Getters
string Flashcard::getFront() const {
    return front;
}
string Flashcard::getBack() const {
    return back;
}
int Flashcard::getDifficulty() const {
    return difficulty;
}