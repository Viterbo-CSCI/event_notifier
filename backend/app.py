from flask import Flask, session, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

app.secret_key = 'my_secret_key'

users = [] # Simulate a user database

@app.route('/api/home')
def home():
    return render_template('home.html') # Render the home.html template

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json() # Get JSON data from the request
    if not data or 'password' not in data or 'email' not in data: # Check if password and email are provided
        return jsonify({'error': 'Invalid input'}), 400 # Bad request if input is invalid
    
    for user in users: # Check if the user already exists
        if user['email'] == data['email']:
            return jsonify({'error': 'Email already registered'}), 409

    # Simulate saving user
    user = {
        'email': data['email'],
        'password': data['password']
    }
    users.append(user)

    return jsonify({'message': 'User registered successfully', 'user': user}), 201


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate input
    if not data or 'password' not in data or 'email' not in data:
         return jsonify({'error': 'Invalid input'}), 400

    # Search for matching user
    for user in users:
            if user['password'] == data['password'] and user['email'] == data['email']:
                return jsonify({'message': 'Login successful'}), 200
            session['email'] = user['email'] # Store email in session
            # No match found
            return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    try:
        pass
    except Exception as e:
        return {"error": str(e)}, 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
