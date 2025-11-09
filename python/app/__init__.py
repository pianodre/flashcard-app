from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
    app.config['DEBUG'] = True
    
    # Register routes
    from app.routes import main
    app.register_blueprint(main)
    
    return app