from flask import Flask, session, request, jsonify
from flask_cors import CORS
from models import UserAccount, UserStore, Event, RSVPStatus, NotificationService
import uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'my_secret_key'
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

user_store = UserStore()
event_store = {}  # Use a simple dictionary to store events
notifier = NotificationService()

@app.route('/api/hello')
def hello():
    return {"message": "Hello from Flask!"}

@app.route('/api/login', methods=['POST'])
def login():
    try:
        # Simulated login
        session['user'] = 'test_user'
        session['password'] = 'test_password'
        return {"message": "User logged in successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 401

@app.route('/api/logout', methods=['POST'])
def logout():
    try:
        session.clear()
        return {"message": "User logged out successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 401

@app.route('/api/users', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data['email']
    phone = data.get('phone', '')
    
    if user_store.getUserByEmail(email):
        return jsonify({"error": "User already exists"}), 400

    user = UserAccount(email=email, phone=phone)
    user_store.addUser(user)
    user_store.save()
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/api/events', methods=['POST'])
def create_event():
    data = request.get_json()
    host = user_store.getUserByEmail(data['hostEmail'])
    if not host:
        return jsonify({"error": "Host user not found"}), 404

    event_id = str(uuid.uuid4())
    event = Event(
        id=event_id,
        title=data['title'],
        location=data['location'],
        dateTime=datetime.fromisoformat(data['dateTime']),
        host=host
    )
    event_store[event_id] = event
    return jsonify({"message": "Event created", "eventId": event_id}), 201

@app.route('/api/events/<event_id>/rsvp', methods=['POST'])
def rsvp_to_event(event_id):
    data = request.get_json()
    user = user_store.getUserByEmail(data['email'])
    if not user:
        return jsonify({"error": "User not found"}), 404

    event = event_store.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    try:
        status = RSVPStatus[data['status']]
    except KeyError:
        return jsonify({"error": "Invalid RSVP status"}), 400

    event.addRSVP(user, status)
    notifier.notifyHostOfRSVP(event, user, status)
    return jsonify({"message": f"RSVP '{status.name}' recorded"}), 200

@app.route('/api/events', methods=['GET'])
def list_events():
    return jsonify([
        {
            "id": event.id,
            "title": event.title,
            "location": event.location,
            "dateTime": event.dateTime.isoformat(),
            "host": event.host.email,
            "rsvpCounts": event.getRSVPCount()
        } for event in event_store.values()
    ])

if __name__ == '__main__':
    user_store.load()
    app.run(host='0.0.0.0', port=5003, debug=True)
