// API Helper Functions for Revu Flashcard App

// Get all available decks with statistics
async function getDecks() {
    try {
        const response = await fetch('/api/decks');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data.decks;
    } catch (error) {
        console.error('Error fetching decks:', error);
        throw error;
    }
}

// Get cards for study session from a specific deck
async function getStudyCards(deckName) {
    try {
        const response = await fetch(`/api/study/${encodeURIComponent(deckName)}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching study cards:', error);
        throw error;
    }
}

// Update card difficulty after user rates it
async function updateCardDifficulty(deckName, cardIndex, difficulty) {
    try {
        const response = await fetch('/api/card/difficulty', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                deck_name: deckName,
                card_index: cardIndex,
                difficulty: difficulty
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error updating card difficulty:', error);
        throw error;
    }
}

// Create a new deck
async function createDeck(deckName) {
    try {
        const response = await fetch('/api/deck/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                deck_name: deckName
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error creating deck:', error);
        throw error;
    }
}