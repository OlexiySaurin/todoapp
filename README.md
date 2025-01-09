# To-Do App

A simple yet powerful To-Do application built with Django and enhanced with HTMX for dynamic interactions. This project includes social authentication via Google and GitHub, a RESTful API, and other essential features to provide a robust task management experience.

# Features
## Core Features:

    Task Management:
        Create, read, update, and delete tasks.
        Mark tasks as completed or pending.
    Dynamic Interactions with HTMX:
        Seamless task creation and updates without full-page reloads.

## Authentication:

    Social Authentication:
        Log in with Google or GitHub accounts using django-allauth.
    Session Management:
        Secure authentication and user-specific task visibility.

## RESTful API:

    Full API for task management:
        Endpoints for creating, updating, retrieving, and deleting tasks.
        Authentication-protected API for secure access.
    Built using Django REST framework (DRF).
    Authorization using JWT

# Tech Stack
## Backend:

    Django:
        Core web framework for handling requests and responses.
        Built-in ORM for database interactions.
    Django REST Framework (DRF):
        For creating RESTful APIs.

## Frontend:

    HTMX:
        For dynamic, server-driven updates.
        Minimal JavaScript required for interactive UI.
    Bootstrap 5
        Provides a responsive and modern design.
        Used for styling buttons, forms, modals, and layouts.
    Django Crispy Forms
        Automatically renders Django forms with Bootstrap 5 styling.
        Makes form layouts cleaner and easier to manage.
    Django Widget Tweaks
        Adds flexibility to form customization.
        Easily apply CSS classes, attributes, and placeholders to form fields.

## Authentication:

    django-allauth:
        Authentication by email including email validations using console. Provides Google and GitHub OAuth authentication out-of-the-box.

# Setup Instructions
## Prerequisites

    Python 3.12 or higher
    Django 5.1.4
    pip (Python package installer)
    
## Installation

    Clone the Repository:
        git clone https://github.com/OlexiySaurin/todoapp.git
        cd todoapp
    Create and Activate a Virtual Environment:
        python3 -m venv venv
        source venv/bin/activate  # On Windows: venv\Scripts\activate
    Install all required packages from requirements.txt:
        pip install -r requirements.txt
    Set Up the Database, apply migrations to initialize the database:
        python manage.py migrate
    Run the Development Server: Start the server on http://127.0.0.1:8000:
        python manage.py runserver
        
### (Optional) Configure Social Authentication:
    Add your Google and GitHub OAuth credentials in the Django admin panel or settings file.
    Ensure django-allauth is configured correctly.

# How to Use
## Local Development:
    Access the web app at http://127.0.0.1:8000.
    Use the task management interface to:
        Add new tasks.
        Edit existing tasks inline.
        Mark tasks as completed.
    Log in with Google or GitHub to access user-specific tasks.

## REST API:
    Explore the API endpoints using tools like Postman or cURL.
    Example Endpoints:
        GET /api/tasks/ - Retrieve all tasks for the logged-in user.
        POST /api/tasks/ - Create a new task.
        PUT /api/task/<id>/ - Update an existing task.
        DELETE /api/task/<id>/ - Delete a task.

# Future Improvements

    Add notifications for task deadlines.
    Add more asyncronous UI updates.
    Provide more advanced filtering and search functionality.
    And more...

# Contributing

## Contributions are welcome! To contribute:
    Fork the repository.
    Create a new branch for your feature/bugfix.
    Submit a pull request with detailed information.
## License
    This project is licensed under the MIT License.
    Feel free to use and modify this project as per the terms of the license.
