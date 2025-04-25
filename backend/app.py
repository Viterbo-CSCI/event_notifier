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
 #Change email/ change phone   
import json
with open('data.json', 'r') as file:
    data = json.load(file)
    
def changeEmail(data_list, current_email, new_email):
    #There's probably some edge case that I'm missing for inputted email values, but I can't think of anything
    for entry in data_list: 
        if entry.get("email") == current_email: # finds current email (change to hashing if possible)
            entry["email"] = new_email #changes current email to new email
            with open('data.json', 'w') as file: #changes the json to match the new email
                json.dump(data, file, indent=4)
            return True #"Email successfully changed!"
    return False #"Please enter a valid email"

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
            with open('data.json', 'w') as file: #transfers the data to the json file
                json.dump(data, file, indent=4)
            return True #"Phone number successfully changed!"
    return False #"Please enter a valid phone number"

def convertable_to_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
