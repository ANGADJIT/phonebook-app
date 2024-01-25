# Phonebook API

This project is a simple phonebook API built using Django and Django Rest Framework (DRF). It provides basic CRUD operations for managing contacts with a straightforward contact model. The API supports different databases by configuring the settings.

## Setup Instructions

1. Create a Python virtual environment:

    ```bash
    python -m venv .venv
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Navigate to the 'phonebook' directory:

    ```bash
    cd ./phonebook
    ```

4. Apply migrations to set up the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. If using Visual Studio Code, press F5 to start the project in debug mode. Otherwise, run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the API documentation at [localhost:8000/redoc](http://localhost:8000/redoc) for more information.

## Tech Stack

- Python 3.11.1
- VS Code IDE
- Django Rest Framework (DRF) for building APIs
- SwaggerDocs for API documentation

## API Endpoints

- **POST** `/contact/add`: Add a new contact.
- **GET** `/contact/all`: Retrieve all contacts.
- **PUT** `/contact/update/<uuid:id>`: Update a contact by UUID.
- **GET** `/contact/search?name=<name>`: Search for contacts by name.
- **DELETE** `/contact/delete/<uuid:id>`: Delete a contact by UUID.