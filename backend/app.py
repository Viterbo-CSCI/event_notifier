from flask import Flask, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

app.secret_key = 'my_secret_key'

@app.route('/api/hello')
def hello():
    return {"message": "Hello from Flask!"}

@app.route('/api/login', methods=['POST'])
def login():
    try:
        session['user'] = 'test_user'
        session['password'] = 'test_password'
        return {"message": "User logged in successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 401

@app.route('/api/logout', methods=['POST'])
def logout():
    try:
        pass
    except Exception as e:
        return {"error": str(e)}, 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
