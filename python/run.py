from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting Revu Flashcard App...")
    print("Access the app at: http://localhost:5554")
    app.run(debug=True, host='0.0.0.0', port=5554)