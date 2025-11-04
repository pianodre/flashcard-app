#include "Deck.h"

Deck::Deck() { // Constructor
    deckName = "";
    cards = vector<Flashcard>();
} 

Deck::Deck(string name) {
    deckName = name;
    cards = vector<Flashcard>();
}

Deck::~Deck() {} // Destructor

// Getters and Setters
string Deck::getDeckName() {
    return deckName;
}
void Deck::setDeckName(string name) {
    deckName = name;
}

// Additional Functions
void Deck::addFlashcard(const Flashcard& card) {
    cards.push_back(card);
}

vector<Flashcard> Deck::getFlashcards() {
    return cards;
}
Flashcard& Deck::getFlashcardAt(int index) {
    if (index >= 0 && index < cards.size()) {
        return cards[index];
    }
    // Return first card as fallback (should not happen with proper usage)
    return cards[0];
}
int Deck::getFlashcardCount() {
    return cards.size();
}

void Deck::shuffleDeck() {
    random_device rd;
    mt19937 g(rd());
    shuffle(cards.begin(), cards.end(), g);
}

bool compareDifficulty(const Flashcard& a, const Flashcard& b) {
    return a.getDifficulty() > b.getDifficulty(); // Higher difficulty first
}

void Deck::sortByDifficulty() {
    sort(cards.begin(), cards.end(), compareDifficulty);
}

void Deck::shuffleWithinDifficulty() {
    // First sort by difficulty to group them
    sortByDifficulty();
    
    // Then shuffle within each difficulty group
    random_device rd;
    mt19937 g(rd());
    
    int start = 0;
    while (start < cards.size()) {
        int currentDifficulty = cards[start].getDifficulty();
        int end = start;
        
        // Find the end of this difficulty group
        while (end < cards.size() && cards[end].getDifficulty() == currentDifficulty) {
            end++;
        }
        
        // Shuffle this group
        if (end - start > 1) {
            shuffle(cards.begin() + start, cards.begin() + end, g);
        }
        
        start = end;
    }
}

void Deck::printDeck() {
    for (int i = 0; i < cards.size(); i++) {
        cout << cards[i].getFront() << endl;
    }
}

void Deck::listAvailableDecks(const string& folderPath) {
    DIR* dir = opendir(folderPath.c_str());
    if (dir == nullptr) {
        cout << "Could not open directory: " << folderPath << endl;
        return;
    }
    
    struct dirent* entry;
    while ((entry = readdir(dir)) != nullptr) {
        string filename = entry->d_name;
        
        // Skip . and .. directories
        if (filename == "." || filename == "..") {
            continue;
        }
        
        // Check if it's a .txt file
        if (filename.length() > 4 && filename.substr(filename.length() - 4) == ".txt") {
            // Remove .txt extension and print
            string deckName = filename.substr(0, filename.length() - 4);
            cout << deckName << endl;
        }
    }
    
    closedir(dir);
}

void Deck::loadFromFile(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cout << "Could not open file: " << filename << endl;
        return;
    }
    
    string line;
    while (getline(file, line)) {
        // Remove semicolon at the end if present
        if (!line.empty() && line.back() == ';') {
            line.pop_back();
        }
        
        // Parse the line: "Front, Back, Difficulty"
        stringstream ss(line);
        string front, back, diffStr;
        
        if (getline(ss, front, ',') && getline(ss, back, ',') && getline(ss, diffStr)) {
            // Trim whitespace
            front.erase(0, front.find_first_not_of(" \t"));
            front.erase(front.find_last_not_of(" \t") + 1);
            back.erase(0, back.find_first_not_of(" \t"));
            back.erase(back.find_last_not_of(" \t") + 1);
            diffStr.erase(0, diffStr.find_first_not_of(" \t"));
            diffStr.erase(diffStr.find_last_not_of(" \t") + 1);
            
            int difficulty = stoi(diffStr);
            Flashcard card(front, back, difficulty);
            addFlashcard(card);
        }
    }
    
    file.close();
    cout << "Loaded " << getFlashcardCount() << " cards from " << filename << endl;
}

void Deck::saveDeck(const string& filename) {
    ofstream file(filename);
    if (!file.is_open()) {
        cout << "Could not open file for writing: " << filename << endl;
        return;
    }
    
    for (int i = 0; i < cards.size(); i++) {
        file << cards[i].getFront() << ", " 
             << cards[i].getBack() << ", " 
             << cards[i].getDifficulty() << ";" << endl;
    }
    
    file.close();
    cout << "Saved " << getFlashcardCount() << " cards to " << filename << endl;
}