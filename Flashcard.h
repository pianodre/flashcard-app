#ifndef FLASHCARD_H
#define FLASHCARD_H

#include <iostream> 
using namespace std;

class Flashcard {

    public:
        Flashcard(); // Constructor
        Flashcard(string front, string back); // Parameterized constructor
        Flashcard(string front, string back, int difficulty); // Parameterized constructor
        ~Flashcard(); // Destructor

        //getters
        string getFront() const;
        string getBack() const;
        int getDifficulty() const;

        //setters
        void setFront(string front);
        void setBack(string back);
        void setDifficulty(int difficulty);

    private:
        string front;
        string back; 
        int difficulty;


};

#endif