# ResumeAI

ResumeAI is an AI-powered platform that helps job applicants analyze and optimize their resumes to match job descriptions, providing insights into relevant skills, keywords, formatting improvements, and suggestions for increasing the likelihood of success in job applications. This project utilizes a modular Flask backend with scalable architecture to support various core features like authentication, resume parsing, and personalized feedback.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Installation and Setup](#installation-and-setup)
3. [Features](#features)
4. [Directory and File Descriptions](#directory-and-file-descriptions)
5. [Running the Application](#running-the-application)
7. [Future Enhancements](#future-enhancements)
8. [Contributing](#contributing)

---

## Project Structure

The project follows a modular and scalable architecture, designed for ease of navigation and code maintenance. The Flask backend is organized by core functionalities, keeping files concise and focused on specific tasks. Each component has a distinct responsibility, and the application uses Blueprints to organize routes, making it easy to add or modify features without affecting other parts of the codebase.

```
ResumeAI/
│
├── app/
│   ├── __init__.py           # Initializes the Flask app
│   ├── config.py             # Configuration settings for Flask
│   ├── routes/
│   │   ├── __init__.py       # Initializes the routes
│   │   ├── auth.py           # Authentication routes (login, signup)
│   │   └── user.py           # User-related routes
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── auth_controller.py # Handles login/signup logic
│   │   └── user_controller.py # Manages user profile and resume uploads
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py            # User model for database
│   ├── services/
│   │   ├── __init__.py
│   │   └── auth_service.py    # Authentication services (token generation, etc.)
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helper.py          # Utility functions
│   └── extensions.py          # Extensions (e.g., database, JWT)
│
├── main.py                     # Entry point to run the Flask app
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## Installation and Setup

To run the ResumeAI backend, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Anushkakumar10/ResumeAI.git
   cd ResumeAI
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**  
   Open `app/config.py` to add configurations like `SECRET_KEY` and `JWT_SECRET_KEY`.

5. **Initialize the Database**
   ```bash
   python main.py
   ```
   The app will create the database file automatically.

---

## Features

- **User Authentication**: Signup and login functionality with JWT-based token authentication.
- **Resume Analysis** (Planned): Analyze resumes against job descriptions to provide insights on skills, keywords, and formatting.
- **User Profile Management**: Manage profiles and store multiple versions of resumes for various job applications.

---

## Directory and File Descriptions

### `app/`
This is the main application folder containing all the backend code for ResumeAI.

- **`__init__.py`** - Sets up the app, initializes the database, JWT, and loads routes.

- **`config.py`** - Contains the app’s configuration settings, such as the database URI and JWT secret key.

#### `app/routes/`
The routes folder organizes the API endpoints in the app.

- **`auth.py`** - Handles authentication routes (e.g., `/auth/signup`, `/auth/login`).
- **`user.py`** - Manages user-related routes like profile management and resume uploads.

#### `app/controllers/`
The controllers folder handles the core business logic and data processing.

- **`auth_controller.py`** - Implements the signup and login functionalities by handling database queries and password hashing.
- **`user_controller.py`** - Will handle user profile updates, resume storage, and other user-specific actions.

#### `app/models/`
The models folder defines the database schema and ORM models.

- **`user.py`** - Defines the `User` model to represent user data in the database (e.g., username, password, email).

#### `app/services/`
Services provide additional, often reusable functions, such as token generation.

- **`auth_service.py`** - Generates JWT tokens for authenticated users.

#### `app/utils/`
Utilities and helper functions that are used across different modules.

- **`helper.py`** - General helper functions that can assist with common tasks across the app.

#### `app/extensions.py`
This file initializes app extensions like SQLAlchemy and JWT to be used across the app.

### Root Files

- **`main.py`** - The entry point of the application. This file runs the Flask app.
- **`requirements.txt`** - Lists the dependencies needed to run the project.
- **`README.md`** - Documentation file that describes the project and its structure.

---

## Running the Application

To start the Flask application:

1. **Run the App**
   ```bash
   python main.py
   ```

2. **Access the API**  
   The API will be available at `http://127.0.0.1:5000/`.

3. **Testing Endpoints**  
   Use a tool like Postman to test the endpoints.

---

## Future Enhancements

- **Resume Parsing and Analysis**: Implement NLP-based resume parsing to provide skill and keyword analysis.
- **Job Market Insights**: Add functionality to compare applicant skills with job market trends.
- **Admin Dashboard**: Build an admin dashboard to help recruiters find the best applicants.

---

## Contributing

Contributions are welcome! See [Contributing](./docs/contributing.md) learn more on how to contribute.

---
