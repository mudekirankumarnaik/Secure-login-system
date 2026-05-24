# Secure Login System

A beginner-friendly secure login web application developed using Python Flask for cybersecurity and web security learning purposes.

This project demonstrates secure authentication techniques such as password hashing, SQL injection prevention, session management, and user authentication.

---

# Features

- User Registration System
- Secure User Login
- Password Hashing using bcrypt
- SQL Injection Protection
- Session Management
- Logout Functionality
- Basic Input Validation
- SQLite Database Integration

---

# Technologies Used

- Python
- Flask
- SQLite
- bcrypt
- HTML

---

# Security Features Implemented

## Password Hashing

User passwords are securely hashed using bcrypt before storing in the database.

## SQL Injection Protection

Parameterized SQL queries are used to prevent SQL injection attacks.

## Session Management

Flask session handling is used to maintain secure user login sessions.

## Input Validation

Basic validation is implemented for usernames and passwords.

---

# Project Structure

```bash
secure-login-system/
│
├── app.py
├── users.db
├── requirements.txt
├── README.md
│
└── templates/
    ├── register.html
    ├── login.html
    └── dashboard.html
```

---

# Installation

Install required libraries:

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
python app.py
```

---

# Default Local URL

```text
http://127.0.0.1:5000
```

---

# Application Workflow

1. User registers an account
2. Password is hashed using bcrypt
3. User logs into the application
4. Session is created after successful login
5. User accesses dashboard securely
6. User can logout safely

---

# Example Features Demonstration

## Registration

- Create a new user account
- Password stored securely in hashed format

## Login

- Verify username and password securely
- Redirect user to dashboard after successful authentication

## Logout

- Session destroyed after logout

---

# Expected Outcome

The project successfully demonstrates a secure login system with hashed passwords, SQL injection protection, session management, and secure authentication practices.

---

# Future Improvements

- Two-Factor Authentication (2FA)
- Email Verification
- Password Reset System
- CAPTCHA Protection
- User Profile Management
- Deployment on Cloud Server

---

# Disclaimer

This project is developed for educational and authorized cybersecurity learning purposes only.

---

# Author

M. Kiran Kumar Naik

Cybersecurity & Python Enthusiast
```text
http://127.0.0.1:5000
```

## Author

M. Kiran Kumar Naik
