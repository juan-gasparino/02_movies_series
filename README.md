# Movies & TV Shows API

Welcome to the Movies & TV Shows API! This API provides endpoints to manage and explore a collection of movies and TV shows. The API is built using Django Rest Framework (DRF) and is backed by a PostgreSQL database.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete movies and TV shows.
- **Search & Filter**: Search by title and filter by genre.
- **User Management**: Secure endpoints with JSON Web Tokens (JWT) for user authentication.
- **Swagger UI**: Explore the API through a user-friendly Swagger interface available at the base URL.

## Database

This project uses a PostgreSQL database named `movies_series`. The database is structured with two main tables: `Movie` and `Serie`.

## Security

- **JWT Authentication**: The API uses JWT tokens to secure endpoints.
- **Open Access**: GET requests are open to the public.
- **Restricted Access**: POST, PUT, and DELETE requests require admin privileges.

## API Endpoints

- **Movies**
  - `GET /movies/` - List all movies.
  - `GET /movies/{id}/` - Retrieve details of a specific movie.
  - `POST /movies/` - Add a new movie (Admin only).
  - `PUT /movies/{id}/` - Update a movie (Admin only).
  - `DELETE /movies/{id}/` - Delete a movie (Admin only).
  - `POST /movies/{id}/like/` - Like a movie.
  - `POST /movies/{id}/follow/` - Follow a movie.

- **TV Shows**
  - `GET /series/` - List all series.
  - `GET /series/{id}/` - Retrieve details of a specific series.
  - `POST /series/` - Add a new series (Admin only).
  - `PUT /series/{id}/` - Update a series (Admin only).
  - `DELETE /series/{id}/` - Delete a series (Admin only).
  - `POST /series/{id}/like/` - Like a series.
  - `POST /series/{id}/follow/` - Follow a series.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/juan-gasparino/02_movies_series
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:
    ```bash
    python manage.py migrate
    ```

4. Load the example data (optional):
    ```bash
    psql -U your_user -d movies_series -a -f example_data.sql
    ```

5. Run the server:
    ```bash
    python manage.py runserver
    ```