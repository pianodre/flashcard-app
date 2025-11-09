// Main JavaScript - Shared utilities and common functionality

// Global utilities and helper functions
window.RevuApp = {
    // App configuration
    config: {
        autoRefreshInterval: 30000, // 30 seconds
        animationDuration: 300,
        debugMode: false
    },
    
    // Utility functions
    utils: {
        // Format time ago (e.g., "2 minutes ago")
        timeAgo: function(dateString) {
            if (!dateString) return 'Never';
            
            const now = new Date();
            const date = new Date(dateString);
            const diffMs = now - date;
            const diffMins = Math.floor(diffMs / 60000);
            const diffHours = Math.floor(diffMins / 60);
            const diffDays = Math.floor(diffHours / 24);
            
            if (diffMins < 1) return 'Just now';
            if (diffMins < 60) return `${diffMins} minute${diffMins > 1 ? 's' : ''} ago`;
            if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;
            return `${diffDays} day${diffDays > 1 ? 's' : ''} ago`;
        },
        
        // Format next review time (e.g., "in 5 minutes")
        timeUntil: function(dateString) {
            if (!dateString) return 'Not scheduled';
            
            const now = new Date();
            const date = new Date(dateString);
            const diffMs = date - now;
            
            if (diffMs <= 0) return 'Due now';
            
            const diffMins = Math.floor(diffMs / 60000);
            const diffHours = Math.floor(diffMins / 60);
            const diffDays = Math.floor(diffHours / 24);
            
            if (diffMins < 1) return 'Due now';
            if (diffMins < 60) return `in ${diffMins} minute${diffMins > 1 ? 's' : ''}`;
            if (diffHours < 24) return `in ${diffHours} hour${diffHours > 1 ? 's' : ''}`;
            return `in ${diffDays} day${diffDays > 1 ? 's' : ''}`;
        },
        
        // Debounce function for search/input
        debounce: function(func, wait) {
            let timeout;
            return function executedFunction(...args) {
                const later = () => {
                    clearTimeout(timeout);
                    func(...args);
                };
                clearTimeout(timeout);
                timeout = setTimeout(later, wait);
            };
        },
        
        // Show toast notification
        showToast: function(message, type = 'info', duration = 3000) {
            const toast = document.createElement('div');
            toast.className = `toast toast-${type}`;
            toast.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: ${type === 'success' ? '#4CAF50' : type === 'error' ? '#F44336' : '#2196F3'};
                color: white;
                padding: 12px 20px;
                border-radius: 6px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                z-index: 10000;
                font-size: 14px;
                max-width: 300px;
                opacity: 0;
                transform: translateX(100%);
                transition: all 0.3s ease;
            `;
            toast.textContent = message;
            
            document.body.appendChild(toast);
            
            // Animate in
            setTimeout(() => {
                toast.style.opacity = '1';
                toast.style.transform = 'translateX(0)';
            }, 10);
            
            // Auto remove
            setTimeout(() => {
                toast.style.opacity = '0';
                toast.style.transform = 'translateX(100%)';
                setTimeout(() => {
                    if (toast.parentNode) {
                        toast.parentNode.removeChild(toast);
                    }
                }, 300);
            }, duration);
        },
        
        // Copy text to clipboard
        copyToClipboard: function(text) {
            if (navigator.clipboard) {
                navigator.clipboard.writeText(text).then(() => {
                    this.showToast('Copied to clipboard!', 'success');
                });
            } else {
                // Fallback for older browsers
                const textArea = document.createElement('textarea');
                textArea.value = text;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
                this.showToast('Copied to clipboard!', 'success');
            }
        },
        
        // Format number with commas
        formatNumber: function(num) {
            return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
        },
        
        // Get deck icon based on name
        getDeckIcon: function(deckName) {
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
                'Music': '🎵',
                'Programming': '💻',
                'Languages': '🗣️',
                'Biology': '🧬',
                'Chemistry': '⚗️',
                'Physics': '⚛️'
            };
            
            return iconMap[deckName] || '📚';
        }
    },
    
    // Navigation helpers
    navigation: {
        // Go to page with optional animation
        goTo: function(url, animate = true) {
            if (animate) {
                document.body.style.opacity = '0.8';
                setTimeout(() => {
                    window.location.href = url;
                }, 150);
            } else {
                window.location.href = url;
            }
        },
        
        // Go back with animation
        goBack: function() {
            document.body.style.opacity = '0.8';
            setTimeout(() => {
                window.history.back();
            }, 150);
        },
        
        // Refresh page with animation
        refresh: function() {
            document.body.style.opacity = '0.8';
            setTimeout(() => {
                window.location.reload();
            }, 150);
        }
    },
    
    // Local storage helpers
    storage: {
        // Get item from localStorage
        get: function(key, defaultValue = null) {
            try {
                const item = localStorage.getItem(`revu_${key}`);
                return item ? JSON.parse(item) : defaultValue;
            } catch (e) {
                console.warn('Error reading from localStorage:', e);
                return defaultValue;
            }
        },
        
        // Set item in localStorage
        set: function(key, value) {
            try {
                localStorage.setItem(`revu_${key}`, JSON.stringify(value));
                return true;
            } catch (e) {
                console.warn('Error writing to localStorage:', e);
                return false;
            }
        },
        
        // Remove item from localStorage
        remove: function(key) {
            try {
                localStorage.removeItem(`revu_${key}`);
                return true;
            } catch (e) {
                console.warn('Error removing from localStorage:', e);
                return false;
            }
        }
    },
    
    // Initialize app
    init: function() {
        console.log('Revu App initialized');
        
        // Add global keyboard shortcuts
        this.setupKeyboardShortcuts();
        
        // Add global error handling
        this.setupErrorHandling();
        
        // Add page transition effects
        this.setupPageTransitions();
    },
    
    // Setup keyboard shortcuts
    setupKeyboardShortcuts: function() {
        document.addEventListener('keydown', (e) => {
            // Ctrl/Cmd + / for help (future feature)
            if ((e.ctrlKey || e.metaKey) && e.key === '/') {
                e.preventDefault();
                this.utils.showToast('Keyboard shortcuts: Space/Enter to flip cards, 1/2/3 for difficulty', 'info', 5000);
            }
            
            // Escape to go back/home
            if (e.key === 'Escape') {
                if (window.location.pathname !== '/') {
                    this.navigation.goTo('/');
                }
            }
        });
    },
    
    // Setup global error handling
    setupErrorHandling: function() {
        window.addEventListener('error', (e) => {
            if (this.config.debugMode) {
                console.error('Global error:', e.error);
            }
        });
        
        // Handle unhandled promise rejections
        window.addEventListener('unhandledrejection', (e) => {
            if (this.config.debugMode) {
                console.error('Unhandled promise rejection:', e.reason);
            }
        });
    },
    
    // Setup page transitions
    setupPageTransitions: function() {
        // Fade in page on load
        document.addEventListener('DOMContentLoaded', () => {
            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 0.3s ease';
            
            setTimeout(() => {
                document.body.style.opacity = '1';
            }, 50);
        });
    }
};

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    RevuApp.init();
});

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = RevuApp;
}