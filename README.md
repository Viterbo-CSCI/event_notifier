# 📅 Event Planning & RSVP System – MVP

This is a **Minimum Viable Product (MVP)** for a startup client who wants a simple, public-facing event planning and RSVP web app.

---


mkdir backend
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install flask flask-cors flask-mail
pip freeze > requirements.txt
touch app.py

## 🧠 Project Description

You are developing a lightweight, mobile-friendly system where users can:

- Create **public events**
- View a list of upcoming events
- RSVP (Going / Maybe / Not Going)
- Receive **email notifications** when:
  - Someone RSVPs to their event (host)
  - Event details change (guest)

The MVP is meant to be deployed quickly to test with real users.

---

## 🛠️ Tech Stack

- **Frontend:** React
- **Backend:** Flask (Python)
- **Database:** SQLite or PostgreSQL (TBD)
- **Email Service:** Flask-Mail or an external service (e.g., SendGrid)
- **Version Control:** Git + GitHub
- **Optional:** Docker for containerization

---

## ✅ Functional Requirements

The system must allow users to:

- Register and log in (basic auth)
- Create public events (title, time, location, description)
- View a list of all events
- RSVP with a status (Going, Maybe, Not Going)
- See how many people RSVP’d per event
- Receive email notifications:
  - Hosts: when someone RSVPs
  - Guests: when event details change

---

## 🚫 Out of Scope (for MVP)

- Private or invite-only events
- User profiles or settings
- Chat or messaging features
- Event ticketing or payment
- Advanced email customization or scheduling

---

## ⚙️ Non-Functional Requirements

- Responsive, mobile-friendly UI
- Simple, intuitive UX
- RESTful API design for frontend-backend communication
- Email notifications sent in real-time
- Clean codebase with comments and docstrings

---

## 🧱 Agile Development Process

This project follows a **multi-step Agile workflow**:

- Step 1: Analyze client needs and write **user stories**
- Step 2: Define **epics** and organize the backlog
- Step 3: Conduct **sprint planning**
- Step 4: Design with **UML diagrams** (Use Case + Class)

---

## 🚀 MVP Sprint 1 Goal

Your goal for Sprint 1 is to deliver:

- Working user registration and login
- Event creation and display
- Basic RSVP functionality
- Email alerts for RSVP actions

Keep it simple, clean, and focused on user needs.
