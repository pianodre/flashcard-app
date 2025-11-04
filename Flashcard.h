#ifndef FLASHCARD_H
#define FLASHCARD_H

#include <iostream> 
using namespace std;

class Flashcard {

    public:
        Flashcard(); // Constructor
        Flashcard(string front, string back); // Parameterized constructor
        ~Flashcard(); // Destructor

        //getters
        string getFront();
        string getBack();
        int getDifficulty();
        int getTimesCorrect();
        int getTimesIncorrect();
        int getConsecutiveCorrect();

        //setters
        void setFront(string front);
        void setBack(string back);
        void setDifficulty(int difficulty);
        void setTimesCorrect(int timesCorrect);
        void setTimesIncorrect(int timesIncorrect);
        void setConsecutiveCorrect(int consecutiveCorrect);

    private:
        string front;
        string back; 
        int difficulty;
        int timesCorrect;
        int timesIncorrect;
        int consecutiveCorrect;


};

#endif