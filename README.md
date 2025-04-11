# Let's generate a beginner-friendly README for the current project
readme_content = """
# 📅 Event Planning & RSVP System – MVP

This is a beginner-friendly **Event Planning & RSVP System**, built as an educational project using Python, Flask, and React. It demonstrates core software engineering concepts such as object-oriented programming, serialization, and web service design.

---

## 🧠 Project Overview

Users can:
- Create public events
- RSVP to events with status (Going, Maybe, NotGoing)
- View their event info
- Be notified of changes or RSVP updates via a notification system

All data is stored **in memory** using Python objects and persisted with `pickle` files (no database required).

---

## 🧱 Core Technologies

- **Backend:** Python, Flask
- **Frontend:** React (using Axios to call Flask API)
- **Persistence:** Python `pickle` module
- **Modeling:** UML-driven class design

---

## 🧩 UML-Based Class Design

### `UserAccount`
Represents a registered user.

| Attribute     | Type    | Description               |
|---------------|---------|---------------------------|
| email         | String  | User's email address      |
| phone         | String  | User's phone number       |
| valid         | Boolean | Whether the account is active |

| Method              | Description                                   |
|---------------------|-----------------------------------------------|
| `login()`           | Authenticates the user                        |
| `logout()`          | Logs the user out (clears session/token)      |
| `getAccountInfo()`  | Returns user info as string or dict           |
| `changeInfo()`      | Updates email and/or phone number             |

---

### `UserStore`
Manages a collection of `UserAccount` objects.

| Attribute     | Type                         | Description                          |
|---------------|------------------------------|--------------------------------------|
| usersByEmail  | `dict<email, UserAccount>`   | Stores users keyed by their email    |

| Method              | Description                                   |
|---------------------|-----------------------------------------------|
| `addUser()`         | Adds a new user to the store                  |
| `getUserByEmail()`  | Retrieves user by email                       |
| `getAllUsers()`     | Lists all users                               |
| `save()`            | Saves all users to a file using `pickle`      |
| `load()`            | Loads users from file at startup              |

---

### `Event`
Represents a hosted event.

| Attribute     | Type                          | Description                            |
|---------------|-------------------------------|----------------------------------------|
| id            | String                        | Unique event identifier                |
| title         | String                        | Title of the event                     |
| location      | String                        | Where the event is hosted              |
| dateTime      | DateTime                      | When the event occurs                  |
| host          | UserAccount                   | The user who created the event         |
| rsvpList      | `dict<UserAccount, RSVPStatus>` | Tracks RSVPs by user                  |

| Method              | Description                                   |
|---------------------|-----------------------------------------------|
| `getInfo()`         | Returns formatted event info                  |
| `addRSVP()`         | Adds or updates RSVP for a user               |
| `edit()`            | Updates title, location, or date/time         |
| `getRSVPCount()`    | Returns RSVP counts by status                 |

---

### `NotificationService`
Simulates sending emails to users.

| Method                        | Description                                        |
|-------------------------------|----------------------------------------------------|
| `sendEmail()`                 | Simulates sending an email                         |
| `notifyHostOfRSVP()`          | Informs host when someone RSVPs                    |
| `notifyGuestsOfChange()`      | Informs all guests of changes to event details     |

---

### `RSVPStatus` (Enum)
Used to track RSVP response status.

| Value        | Meaning        |
|--------------|----------------|
| `Going`      | User is attending |
| `Maybe`      | User might attend |
| `NotGoing`   | User is not attending |

---

## 🔁 System Relationships

- `UserAccount` creates `Event` (host is a user)
- `UserAccount` RSVPs to `Event`
- `UserStore` manages many `UserAccount` instances
- `Event` tracks RSVPs using `UserAccount` and `RSVPStatus`
- `NotificationService` interacts with `UserAccount` and `Event`

---

## 🚀 Project Goals

This system is used to:
- Teach object-oriented design and UML modeling
- Practice building RESTful APIs with Flask
- Understand state persistence without databases
- Integrate frontend/backend communication using JSON
- Simulate real-world features like RSVP management and notifications

---

## 📝 Getting Started (Coming Soon)
Instructions for running the Flask backend, React frontend, and testing routes will be added here.

---

## 📦 Persistence

All user data is stored in memory and saved to disk using Python’s `pickle` module in `users.pkl`. This makes it easy to reload users after restarting the server.

---

## 💡 Notes for Students

- The app currently has no login sessions or tokens — it's for learning structure, not production auth
- Events and notifications are also stored in memory (no real email)
- Classes follow UML closely to demonstrate good design patterns

---

## 📈 Next Steps (Future Epics)

- Event creation and editing
- RSVP submission UI
- Notification handling and templates
- Guest email import (CSV or list input)
"""

# Save the README to file
readme_path = Path("/mnt/data/README_Event_Planner.md")
readme_path.write_text(readme_content.strip())
readme_path
