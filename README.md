# SurviceBuddy

A simple rule-based chatbot web application built using **Flask**, **NLTK**, and **HTML templates**, with basic user login and session management.  
The bot matches user input with predefined patterns stored in `intents1.json` and responds with appropriate messages.

---

## Features

- **User authentication**  
  - Login, Register, and Logout system (using in-memory user store).  
- **Session-based chat history**  
  - Each user session maintains its own conversation log.  
- **Rule-based chatbot**  
  - Matches user input to intents using token overlap logic.  
- **Flask-powered web app**  
  - HTML templates for login, registration, and chat interface.  

---

## Folder Structure

project/
├── app.py # Main Flask application
├── intents1.json # Chatbot training data (patterns and responses)
├── requirements.txt # Python dependencies
├── templates/
│ ├── base.html # Base template for inheritance
│ ├── login.html # Login page
│ ├── register.html # Registration page
│ └── index.html # Chat interface
└── static/
└── css/
└── style.css # Custom CSS styles

---

## Requirements

- Python 3.8+
- Virtual environment recommended

Dependencies:
- Flask  
- nltk  

You can install them all with:

pip install -r requirements.txt
Setup Instructions
Clone or download this repository


git clone https://github.com/yourusername/servicebuddy.git
cd servicebuddy
Create and activate a virtual environment (optional but recommended)

python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
Install dependencies


pip install -r requirements.txt
Download NLTK data (only required once)

import nltk
nltk.download('punkt')
Run the Flask app

python app.py
By default, the app runs at http://127.0.0.1:5000.

Usage
Open the app in your browser at http://127.0.0.1:5000.

Register a new account or login with:

Username: testuser

Password: password123

Start chatting with the bot! Your messages and the bot responses will appear in the chat history panel.

Important Notes
Secret Key:
Update app.secret_key in app.py with a strong, random key before deploying to production.

User Store:
User credentials are currently stored in-memory (users dictionary).
This is NOT secure for production. Replace with a real database (e.g., SQLite, PostgreSQL).

File Paths:
The app automatically loads intents1.json relative to the project directory using:


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.path.join(BASE_DIR, 'intents1.json')
This avoids issues with relative vs. absolute paths.

Customization
Modify intents:
Edit intents1.json to add new patterns and responses.

Improve chatbot logic:
Replace the token-overlap matcher with ML models or use nltk classifiers for better accuracy.

Frontend:
Customize HTML templates in templates/ to change the design.

License
This project is for educational purposes.
Feel free to use and modify it, but do not deploy without adding proper security measures.

Author

Amit Paul
Built with ❤️ using Python , NLTK and Flask.
