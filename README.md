# Django REST Framework Blog App

This project is a blog application built using **Python**, **Django**, and **Django Rest Framework (DRF)**. It serves as a practical example of the skills I gained through the "Python Django with API Development" course on Miuul, where I learned how to design and implement modern APIs using Django and DRF.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Future Improvements](#future-improvements)
- [Setup and Installation](#setup-and-installation)

## Project Overview
The **Django REST Framework Blog App** demonstrates the process of building and deploying secure, reliable, and efficient APIs. It allows users to create, read, update, and delete blog posts. The app also integrates secure token-based authentication (JWT), pagination, error handling, and API documentation.

This project was developed as part of my journey to understand the core principles of API development and to put theory into practice. The knowledge gained from this course helped me build a robust backend solution for handling blog data.

## Features
- **User Authentication**: JWT-based authentication for secure login and access control.
- **CRUD Operations**: Full Create, Read, Update, and Delete functionality for managing blog posts.
- **Pagination**: Efficient data retrieval with paginated responses.
- **Error Handling**: Proper error handling and validation for better user experience.
- **API Documentation**: Detailed API documentation to provide clear guidelines for developers.
- **Postman Testing**: APIs were tested using Postman to ensure accuracy and performance.

## Technologies Used
- **Python**: Backend programming language.
- **Django**: Web framework used to build the application.
- **Django REST Framework (DRF)**: Framework for building APIs.
- **JWT**: JSON Web Tokens for secure authentication.
- **Postman**: Tool used for API testing.
- **SQLite**: Default database used for this application.

## Usage
- **Access the Admin Panel**: Go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.
- **Test APIs**: Use Postman or any other API testing tool to test the available endpoints. API documentation is available to help you with the request format.

## API Endpoints
Here are some of the key API endpoints in the project:

- `POST /api/auth/login/`: Login and obtain a JWT token.
- `POST /api/posts/`: Create a new blog post (requires authentication).
- `GET /api/posts/`: List all blog posts with pagination.
- `GET /api/posts/{id}/`: Get a specific blog post by ID.
- `PUT /api/posts/{id}/`: Update an existing blog post (requires authentication).
- `DELETE /api/posts/{id}/`: Delete a specific blog post (requires authentication).

## Testing
During the development of this application, I extensively used **Postman** to test the APIs. This helped ensure the functionality and performance of the API endpoints, as well as the proper handling of edge cases and error scenarios.

## Future Improvements
While this project covers the core functionality, here are some potential areas for improvement:
- **User Profile Management**: Add features for users to manage their profiles.
- **Commenting System**: Implement a comment system where users can interact with blog posts.
- **Search Functionality**: Add the ability to search blog posts by title, tags, or content.
- **Unit Tests**: Add comprehensive unit tests for the application to ensure robust performance.

## Setup and Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-HasanCan6241/django-rest-framework-blog-app.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd django-rest-framework-blog-app
    ```

3. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser** (for admin access):
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the server**:
    ```bash
    python manage.py runserver
    ```
