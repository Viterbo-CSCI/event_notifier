import json

class UserAccount:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.logged_in = True
        
    def logout(self):
        self.logged_in = False
        print(f"{self.username} has logged out.")
        
    def getAccountInfo(self):
        return {
            "username": self.username,
            "email": self.email,
            "logged_in": self.logged_in
        }
    
user = UserAccount("john_doe", "john@example.com")
print(json.dumps(user.getAccountInfo(), indent=2))