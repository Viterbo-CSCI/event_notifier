# test_app.py
import json
from app import app, users  # Import the users list to prepopulate it

def test_login():
    # Prepopulate the users list with a test user
    users.append({
        'email': 'bob@example.com',
        'password': '1234'
    })

    with app.test_client() as client:
        response = client.post('/api/login', data=json.dumps({'password':'1234','email':'bob@example.com'}),
        content_type='application/json')

        # Assert the response status code
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        # Assert the response JSON
        assert response.json == {'message': 'Login successful'}, f"Unexpected response: {response.json}"

        print("Test passed!")

def test_register():
    # Prepopulate the users list with a test user
    users.append({
        'email': 'bob@example.com',
        'password': '1234'
    })

    with app.test_client() as client:
        response = client.post('/api/login', data=json.dumps({'password':'1234','email':'bob@example.com'}),
        content_type='application/json')

        # Assert the response status code
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        # Assert the response JSON
        assert response.json == {'message': 'Login successful'}, f"Unexpected response: {response.json}"

        print("Test passed!")

if __name__ == '__main__':
    test_login()