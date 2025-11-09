// Flashcard Study Session JavaScript

// Global variables for study session
let currentDeck = null;
let studyCards = [];
let currentCardIndex = 0;
let isCardFlipped = false;

// Initialize flashcard page when DOM loads
document.addEventListener('DOMContentLoaded', async () => {
    console.log('Flashcard page loaded');
    
    // Get deck name from URL or use default
    const deckName = getDeckNameFromURL() || 'spanish_vocab';
    
    // Load study session
    await loadStudySession(deckName);
    
    // Set up event listeners
    setupEventListeners();
});

// Extract deck name from URL path
function getDeckNameFromURL() {
    const path = window.location.pathname;
    const parts = path.split('/');
    // URL format: /study/deck_name
    return parts[2] || null;
}

// Load study session with cards
async function loadStudySession(deckName) {
    try {
        console.log(`Loading study session for: ${deckName}`);
        
        // Get study cards from API
        const studyData = await getStudyCards(deckName);
        
        // Use the URL deck name (not the display name) for API calls
        currentDeck = deckName;  // Use URL name, not studyData.deck_name
        studyCards = studyData.cards;
        currentCardIndex = 0;
        
        console.log(`Loaded ${studyCards.length} cards for study`);
        
        if (studyCards.length === 0) {
            showNoCardsMessage();
            return;
        }
        
        // Display first card
        displayCurrentCard();
        updateProgressInfo();
        
    } catch (error) {
        console.error('Error loading study session:', error);
        showErrorMessage('Failed to load study session. Please try again.');
    }
}

// Display the current card
function displayCurrentCard() {
    if (!studyCards || studyCards.length === 0) return;
    
    const card = studyCards[currentCardIndex];
    const flashcardElement = document.getElementById('flashcard');
    const questionElement = flashcardElement.querySelector('.card-front .card-content');
    const answerElement = flashcardElement.querySelector('.card-back .card-content');
    
    // Update card content
    questionElement.textContent = card.question;
    answerElement.textContent = card.answer;
    
    // Reset card to front side
    flashcardElement.classList.remove('flipped');
    isCardFlipped = false;
    
    // Hide difficulty buttons initially
    hideDifficultyButtons();
}

// Update progress indicator
function updateProgressInfo() {
    const progressElement = document.querySelector('.progress-info');
    if (progressElement && studyCards.length > 0) {
        progressElement.textContent = `Card ${currentCardIndex + 1} of ${studyCards.length}`;
    }
}

// Set up event listeners
function setupEventListeners() {
    // Card flip on click
    const flashcard = document.getElementById('flashcard');
    if (flashcard) {
        flashcard.addEventListener('click', flipCard);
    }
    
    // Difficulty buttons
    const hardBtn = document.querySelector('.btn-hard');
    const mediumBtn = document.querySelector('.btn-medium');
    const easyBtn = document.querySelector('.btn-easy');
    
    if (hardBtn) hardBtn.addEventListener('click', () => rateDifficulty(1));
    if (mediumBtn) mediumBtn.addEventListener('click', () => rateDifficulty(2));
    if (easyBtn) easyBtn.addEventListener('click', () => rateDifficulty(3));
}

// Flip the flashcard
function flipCard() {
    const flashcardElement = document.getElementById('flashcard');
    
    if (!isCardFlipped) {
        // Flip to answer side
        flashcardElement.classList.add('flipped');
        isCardFlipped = true;
        
        // Show difficulty buttons
        showDifficultyButtons();
    }
}

// Show difficulty buttons
function showDifficultyButtons() {
    const buttonsContainer = document.querySelector('.difficulty-buttons');
    if (buttonsContainer) {
        buttonsContainer.style.display = 'flex';
        buttonsContainer.style.opacity = '1';
    }
}

// Hide difficulty buttons
function hideDifficultyButtons() {
    const buttonsContainer = document.querySelector('.difficulty-buttons');
    if (buttonsContainer) {
        buttonsContainer.style.display = 'none';
        buttonsContainer.style.opacity = '0';
    }
}

// Rate card difficulty and move to next card
async function rateDifficulty(difficulty) {
    if (!isCardFlipped || !studyCards || studyCards.length === 0) return;
    
    try {
        const card = studyCards[currentCardIndex];
        
        console.log(`Rating card difficulty: ${difficulty}`);
        
        // Update card difficulty via API
        await updateCardDifficulty(currentDeck, card.id, difficulty);
        
        console.log('Card difficulty updated successfully');
        
        // Move to next card
        moveToNextCard();
        
    } catch (error) {
        console.error('Error updating card difficulty:', error);
        showErrorMessage('Failed to save progress. Please try again.');
    }
}

// Move to the next card or finish session
function moveToNextCard() {
    currentCardIndex++;
    
    if (currentCardIndex >= studyCards.length) {
        // Study session complete
        showSessionComplete();
    } else {
        // Display next card
        displayCurrentCard();
        updateProgressInfo();
    }
}

// Show session complete message
function showSessionComplete() {
    const mainContent = document.querySelector('.main-content');
    if (mainContent) {
        mainContent.innerHTML = `
            <div class="session-complete">
                <h1>🎉 Study Session Complete!</h1>
                <p>Great job! You've reviewed all ${studyCards.length} cards.</p>
                <div class="session-actions">
                    <button onclick="window.location.href='/study'" class="btn-primary">
                        📚 Study Another Deck
                    </button>
                    <button onclick="window.location.href='/'" class="btn-secondary">
                        🏠 Go Home
                    </button>
                </div>
            </div>
        `;
    }
}

// Show no cards message
function showNoCardsMessage() {
    const mainContent = document.querySelector('.main-content');
    if (mainContent) {
        mainContent.innerHTML = `
            <div class="no-cards">
                <h1>📭 No Cards Due for Review</h1>
                <p>All cards in this deck are up to date!</p>
                <div class="session-actions">
                    <button onclick="window.location.href='/study'" class="btn-primary">
                        📚 Choose Another Deck
                    </button>
                    <button onclick="window.location.href='/'" class="btn-secondary">
                        🏠 Go Home
                    </button>
                </div>
            </div>
        `;
    }
}

// Show error message
function showErrorMessage(message) {
    const mainContent = document.querySelector('.main-content');
    if (mainContent) {
        mainContent.innerHTML = `
            <div class="error-message">
                <h1>❌ Error</h1>
                <p>${message}</p>
                <div class="session-actions">
                    <button onclick="window.location.reload()" class="btn-success">
                        🔄 Try Again
                    </button>
                    <button onclick="window.location.href='/'" class="btn-secondary">
                        🏠 Go Home
                    </button>
                </div>
            </div>
        `;
    }
}

// Keyboard shortcuts (optional enhancement)
document.addEventListener('keydown', (event) => {
    if (!isCardFlipped) {
        // Space or Enter to flip card
        if (event.code === 'Space' || event.code === 'Enter') {
            event.preventDefault();
            flipCard();
        }
    } else {
        // Number keys for difficulty rating
        switch (event.code) {
            case 'Digit1':
                event.preventDefault();
                rateDifficulty(1); // Hard
                break;
            case 'Digit2':
                event.preventDefault();
                rateDifficulty(2); // Medium
                break;
            case 'Digit3':
                event.preventDefault();
                rateDifficulty(3); // Easy
                break;
        }
    }
});