
from flask import Flask, session
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
    # This should only return 1 item beause ID is unique
    def get_by_id(self, event_id):
        if event_id in self._event_index:
            return self._events[self._event_index[event_id]]
        return None
    
    # This should return all items with the title isn't unique
    def get_by_title(self, title):
        return [event for event in self._events if event.title == title]
    
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
    
import json
with open('data.json', 'r') as f:
    data = json.load(f)
@app.route('/api/changeEmail', methods=['POST'])    
def changeEmail(data_list, current_email, new_email):
    #There's probably some edge case that I'm missing for inputted email values, but I can't think of anything
    for entry in data_list: 
        if entry.get("email") == current_email: # finds current email (change to hashing if possible)
            entry["email"] = new_email #changes current email to new email
            with open('data.json', 'w') as f: #changes the json to match the new email
                json.dump(data, f, indent=4)
            return True #"Email successfully changed!"
    return False #"Please enter a valid email"
@app.route('/api/changePhone', methods=['POST']) 
def changePhone(data_list, current_phone, new_phone):
    if current_phone[3] == "-" or current_phone[3] == " " and current_phone[7] == "-" or current_phone[7] == " ": #checks if current phone has common separators and sets it to just numbers
        indices = [0, 1, 2, 4, 5, 6, 8, 9, 10, 11]
        current_phone = ''.join([current_phone[i] for i in indices])
        
    if new_phone[3] == "-" or new_phone[3] == " " and new_phone[7] == "-" or new_phone[7] == " ": # checks if new_phone has common separators and sets it to just numbers
        indices = [0, 1, 2, 4, 5, 6, 8, 9, 10, 11]
        new_phone = ''.join([new_phone[i] for i in indices])
        
    if len(current_phone) != 10 or len(new_phone) != 10: #checks to see if phone number is proper length
        print("length error")
        return False #"Please enter a valid phone number"
    
    if convertable_to_integer(current_phone) == False or convertable_to_integer(new_phone) == False: #checks if the phone number has a non-number in it (perhaps redundant if the user can only enter in numbers)
        print("Character error")
        return False #"Please enter a valid phone number"
    
    for entry in data_list: 
        if entry.get("phone") == current_phone: # finds the current phone number.
            entry["phone"] = new_phone #changes the current phone number to the new one
            with open('data.json', 'w') as f: #transfers the data to the json file
                json.dump(data, f, indent=4)
            return True #"Phone number successfully changed!"
    return False #"Please enter a valid phone number"

def convertable_to_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False