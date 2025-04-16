from flask import Flask, session, request, jsonify
from flask_cors import CORS
import os
import pickle

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

class Event:
    def __init__(self, id, title, location, dateTime, rsvpList, host):
        self.id = id
        self.title = title
        self.location = location
        self.dateTime = dateTime
        self.rsvpList = rsvpList
        self.host = host
    
    def to_dict(self):
        """Convert event to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'location': self.location,
            'dateTime': self.dateTime,
            'rsvpList': self.rsvpList,
            'host': self.host
        }

class EventStore:
    def __init__(self, file_path='events.pkl'):
        self.file_path = file_path
        self._events = []
        self._event_index = {}
    
    def load_all(self):
        """Load all events from disk using pickle"""
        self._events = []
        self._event_index = {}
        
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
            try:
                with open(self.file_path, 'rb') as f:
                    self._events = pickle.load(f)
                    for i, event in enumerate(self._events):
                        self._event_index[event.id] = i
                return self._events
            except Exception as e:
                print(f"Error loading events: {str(e)}")
                return []
        return []
    
    def save(self, event):
        if self.id_exists(event.id):
            raise ValueError(f"Event with ID {event.id} already exists")
        
        self._events.append(event)
        self._event_index[event.id] = len(self._events) - 1
        
        self.save_all()
        
    def save_all(self):
        with open(self.file_path, 'wb') as f:
            pickle.dump(self._events, f)
    
    def id_exists(self, event_id):
        return event_id in self._event_index
    
    def get_by_id(self, event_id):
        if event_id in self._event_index:
            return self._events[self._event_index[event_id]]
        return None
    
    def get_all(self):
        return self._events

event_store = EventStore()

@app.route('/api/events', methods=['POST'])
def create_events():
    try:
        event_data = request.get_json()
        if not event_data:
            return {"error": "No data provided or invalid JSON"}, 400
            
        print(f"Received event data: {event_data}")

        #TODO Automatically generate ID
        
        required_fields = ['id', 'title', 'location', 'dateTime', 'rsvpList', 'host']
        for field in required_fields:
            if field not in event_data:
                return {"error": f"Missing required field: {field}"}, 400
        
        # Validations
        if not isinstance(event_data['id'], str) or not event_data['id'].strip():
            return {"error": "Event ID must be a non-empty string"}, 400
            
        if not isinstance(event_data['title'], str) or not event_data['title'].strip():
            return {"error": "Event title must be a non-empty string"}, 400
            
        if not isinstance(event_data['rsvpList'], list):
            return {"error": "RSVP list must be an array"}, 400
            
        if event_store.id_exists(event_data['id']):
            return {"error": "Event ID must be unique"}, 400
        
        new_event = Event(
            event_data['id'],
            event_data['title'],
            event_data['location'],
            event_data['dateTime'],
            event_data['rsvpList'],
            event_data['host']
        )
        
        event_store.save(new_event)
        
        return {
            "message": "Event created successfully",
            "event": new_event.to_dict()
        }, 201
    except ValueError as ve:
        print(f"Validation error creating event: {str(ve)}")
        return {"error": str(ve)}, 400
    except Exception as e:
        print(f"Error creating event: {str(e)}")
        return {"error": str(e)}, 500

@app.route('/api/events/<event_id>', methods=['GET'])
def get_event(event_id):
    try:
        event = event_store.get_by_id(event_id)
        if event is None:
            return {"error": "Event not found"}, 404
        return jsonify(event.to_dict()), 200
    except Exception as e:
        print("Error retrieving event:", str(e))
        return {"error": str(e)}, 500
    
@app.route('/api/events', methods=['GET'])
def get_events():
    try:
        events = event_store.get_all()
        event_dicts = [event.to_dict() for event in events]
        return jsonify(event_dicts), 200
    except Exception as e:
        print("Error retrieving events:", str(e))
        return {"error": str(e)}, 500


if __name__ == '__main__':
    event_store.load_all()
    app.run(host='0.0.0.0', port=5003, debug=True)
