from flask import Flask
from flask_cors import CORS
from flask import Flask, request, jsonify
from enum import Enum

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route('/api/hello')
def hello():
    return {"message": "Hello from Flask!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

class RSVPStatus(str, Enum):
    GOING = "Going"
    MAYBE = "Maybe"
    NOT_GOING = "NotGoing"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/rsvp", methods=["POST"])
def rsvp():
    data = request.get_json()

    name = data.get("name")
    event_id = data.get("event_id")
    status = data.get("status")

    if not all([name, event_id, status]):
        return jsonify({"error": "Missing fields"}), 400

    if status not in [s.value for s in RSVPStatus]:
        return jsonify({"error": "Invalid RSVP status"}), 400

    return jsonify({
        "message": f"{name} RSVP'd as {status} for event {event_id}"
    })

if __name__ == "__main__":
    app.run(debug=True)
