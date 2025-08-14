import json
import nltk
from nltk.tokenize import word_tokenize
import random
from flask import Flask, render_template, request, jsonify, redirect, url_for, session

# Download necessary NLTK data (only needs to be run once)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

app = Flask(__name__)
app.secret_key = 'your_super_secret_key_here' # CHANGE THIS TO A STRONG, RANDOM KEY!

# --- Chatbot Logic (from your provided code - unchanged) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def load_intents(file_path=os.path.join(BASE_DIR, 'intents1.json')):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def tokenize_sentence(sentence):
    tokens = word_tokenize(sentence.lower())
    return tokens

def get_intent(user_input, intents):
    tokens = tokenize_sentence(user_input)
    best_match = None
    highest_overlap = 0
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern_tokens = tokenize_sentence(pattern.lower())
            if user_input == pattern.lower():
                return intent['tag'], intent['responses']
            overlap = len(set(tokens) & set(pattern_tokens))
            if overlap > highest_overlap:
                highest_overlap = overlap
                best_match = (intent['tag'], intent['responses'])
    if best_match:
        return best_match
    return None, ["I'm sorry, I don't understand that."]

def get_response(responses):
    return random.choice(responses)

def chatbot_response(user_input):
    intents = load_intents()
    intent, responses = get_intent(user_input, intents)
    response = get_response(responses)
    return response

# --- User Management (Simple in-memory for demonstration) ---
users = {
    "testuser": "password123", # Example user
    "admin": "adminpass"
}

# --- Flask Routes ---

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('chatbot_page'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            session['chat_history'] = [] # Initialize chat history for new session
            return redirect(url_for('chatbot_page'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('register.html', error='Username already exists')
        else:
            users[username] = password
            session['username'] = username
            session['chat_history'] = [] # Initialize chat history for new session
            return redirect(url_for('chatbot_page'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('chat_history', None) # Clear chat history on logout
    return redirect(url_for('login'))

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot_page():
    if 'username' not in session:
        return redirect(url_for('login'))

    if 'chat_history' not in session:
        session['chat_history'] = [] # Ensure chat_history exists

    if request.method == 'POST':
        user_message = request.form.get('user_input')
        if user_message:
            # Add user message to history
            session['chat_history'].append({'sender': 'user', 'message': user_message})
            
            # Get bot response
            bot_reply = chatbot_response(user_message)
            session['chat_history'].append({'sender': 'bot', 'message': bot_reply})
            
            # Ensure session is saved (important for modifying lists/dicts in session)
            session.modified = True 
            
    # Always render the template with the current chat history
    return render_template('index.html', username=session['username'], chat_history=session['chat_history'])

if __name__ == '__main__':
    app.run(debug=True)
