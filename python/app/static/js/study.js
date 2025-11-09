// Study Page JavaScript - Dynamic Deck Loading

// Initialize study page when DOM loads
document.addEventListener('DOMContentLoaded', async () => {
    console.log('Study page loaded');
    
    // Load and display decks
    await loadDecks();
    
    // Auto-refresh every 30 seconds to show updated due counts
    setInterval(async () => {
        console.log('Auto-refreshing deck data...');
        await loadDecks();
    }, 30000); // 30 seconds
});

// Load all available decks from API
async function loadDecks() {
    try {
        console.log('Loading decks from API...');
        
        // Get decks from API
        const decks = await getDecks();
        
        console.log(`Loaded ${decks.length} decks`);
        
        if (decks.length === 0) {
            showNoDecksMessage();
            return;
        }
        
        // Display decks
        displayDecks(decks);
        
    } catch (error) {
        console.error('Error loading decks:', error);
        showErrorMessage('Failed to load decks. Please try again.');
    }
}

// Display decks in the deck list
function displayDecks(decks) {
    const deckList = document.querySelector('.deck-list');
    if (!deckList) return;
    
    // Clear existing content
    deckList.innerHTML = '';
    
    // Create deck cards
    decks.forEach(deck => {
        const deckCard = createDeckCard(deck);
        deckList.appendChild(deckCard);
    });
}

// Create a deck card element
function createDeckCard(deck) {
    // Create deck card container
    const deckLink = document.createElement('a');
    deckLink.href = `/study/${encodeURIComponent(getDeckFileName(deck.name))}`;
    deckLink.style.textDecoration = 'none';
    deckLink.style.color = 'inherit';
    
    const deckCard = document.createElement('div');
    deckCard.className = 'deck-card';
    
    // Deck info section
    const deckInfo = document.createElement('div');
    deckInfo.className = 'deck-info';
    
    const deckName = document.createElement('div');
    deckName.className = 'deck-name';
    deckName.textContent = deck.name;
    
    const deckStats = document.createElement('div');
    deckStats.className = 'deck-stats';
    deckStats.textContent = deck.description;
    
    deckInfo.appendChild(deckName);
    deckInfo.appendChild(deckStats);
    
    // Deck icon section
    const deckIcon = document.createElement('div');
    deckIcon.className = 'deck-icon';
    deckIcon.textContent = getDeckIcon(deck.name);
    
    // Assemble card
    deckCard.appendChild(deckInfo);
    deckCard.appendChild(deckIcon);
    deckLink.appendChild(deckCard);
    
    return deckLink;
}

// Convert display name to filename format
function getDeckFileName(displayName) {
    // Convert "Spanish Vocabulary" to "spanish_vocab" etc.
    const nameMap = {
        'Spanish Vocabulary': 'spanish_vocab',
        'Python Basics': 'python_basics',
        'Math problems': 'math_problems'
    };
    
    return nameMap[displayName] || displayName.toLowerCase().replace(/\s+/g, '_');
}

// Get appropriate icon for deck
function getDeckIcon(deckName) {
    const iconMap = {
        'Spanish Vocabulary': '🇪🇸',
        'Python Basics': '🐍',
        'Math problems': '📐',
        'Math Formulas': '📐',
        'History Facts': '🏛️',
        'Science': '🔬',
        'Geography': '🌍',
        'Literature': '📚',
        'Art': '🎨',
        'Music': '🎵'
    };
    
    return iconMap[deckName] || '📚'; // Default icon
}

// Show message when no decks are available
function showNoDecksMessage() {
    const deckList = document.querySelector('.deck-list');
    if (!deckList) return;
    
    deckList.innerHTML = `
        <div class="no-decks-message" style="text-align: center; padding: 3rem; color: #666;">
            <h2 style="color: #FF9800; margin-bottom: 1rem;">📭 No Decks Available</h2>
            <p style="font-size: 1.1rem; margin-bottom: 2rem;">You don't have any flashcard decks yet.</p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <button onclick="window.location.href='/'" class="btn-primary">
                    🏠 Go Home
                </button>
                <button onclick="window.location.reload()" class="btn-secondary">
                    🔄 Refresh
                </button>
            </div>
        </div>
    `;
}

// Show error message
function showErrorMessage(message) {
    const deckList = document.querySelector('.deck-list');
    if (!deckList) return;
    
    deckList.innerHTML = `
        <div class="error-message" style="text-align: center; padding: 3rem; color: #666;">
            <h2 style="color: #F44336; margin-bottom: 1rem;">❌ Error Loading Decks</h2>
            <p style="font-size: 1.1rem; margin-bottom: 2rem;">${message}</p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
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

// Add loading indicator (optional enhancement)
function showLoadingIndicator() {
    const deckList = document.querySelector('.deck-list');
    if (!deckList) return;
    
    deckList.innerHTML = `
        <div class="loading-indicator" style="text-align: center; padding: 3rem; color: #666;">
            <div style="font-size: 2rem; margin-bottom: 1rem;">⏳</div>
            <p>Loading your decks...</p>
        </div>
    `;
}

// Refresh decks (can be called by refresh button)
async function refreshDecks() {
    showLoadingIndicator();
    await loadDecks();
}