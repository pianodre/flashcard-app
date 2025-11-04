#include "Flashcard.h"

// Default Constructor
Flashcard::Flashcard(){}

// Overload Constructor
Flashcard::Flashcard(string front, string back) {
    this->front = front;
    this->back = back;
    difficulty = 1;
    timesCorrect = 0;
    timesIncorrect = 0;
    consecutiveCorrect = 0;
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
void Flashcard::setTimesCorrect(int timesCorrect) {
    this->timesCorrect = timesCorrect;
}
void Flashcard::setTimesIncorrect(int timesIncorrect) {
    this->timesIncorrect = timesIncorrect;
}
void Flashcard::setConsecutiveCorrect(int consecutiveCorrect) {
    this->consecutiveCorrect = consecutiveCorrect;
}

// Getters
string Flashcard::getFront() {
    return front;
}
string Flashcard::getBack() {
    return back;
}
int Flashcard::getDifficulty() {
    return difficulty;
}
int Flashcard::getTimesCorrect() {
    return timesCorrect;
}
int Flashcard::getTimesIncorrect() {
    return timesIncorrect;
}
int Flashcard::getConsecutiveCorrect() {
    return consecutiveCorrect;
}