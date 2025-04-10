```markdown
# Late Show API

The **Late Show API** is a Flask-based RESTful API designed to manage episodes, guests, and their appearances on a late-night talk show. It provides endpoints to create, read, update, and delete data for episodes, guests, and their appearances, along with database seeding and migrations.

## Features

- **Episodes Management**: Create, retrieve, update, and delete episodes.
- **Guests Management**: Manage guest information, including their name and occupation.
- **Appearances Management**: Track guest appearances on specific episodes with ratings.
- **Database Seeding**: Populate the database with sample data using the `Faker` library.
- **Database Migrations**: Manage schema changes using Alembic and Flask-Migrate.
- **RESTful API**: Fully RESTful endpoints for CRUD operations.

## Project Structure

```
late-show/
├── app/
│   ├── __init__.py          # App factory and initialization
│   ├── models/              # Models for database tables
│   │   ├── __init__.py      # Import all models here
│   │   ├── episode.py       # Episode model
│   │   ├── guest.py         # Guest model
│   │   ├── appearance.py    # Appearance model
│   ├── routes/              # API routes
│   │   ├── __init__.py      # Import all routes here
│   │   ├── episode.py       # Episode routes
│   │   ├── guest.py         # Guest routes
│   │   ├── appearance.py    # Appearance routes
│   ├── extensions.py        # Extensions like db, migrate
│   ├── config.py            # Configuration for the app
│   ├── seed.py              # Database seeding script
├── migrations/              # Alembic migrations
├── instances/
│   ├── lateShowDb.sqlite3   # SQLite database
├── run.py                   # Entry point for the app
├── Pipfile                  # Dependencies
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd late-show
   ```

2. Install dependencies using `pipenv`:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Set up the database:
   ```bash
   flask db upgrade
   ```

5. Seed the database with sample data:
   ```bash
   python app/seed.py
   ```

6. Run the application:
   ```bash
   python run.py
   ```

## API Endpoints

### Episodes
- `GET /episodes`: Retrieve all episodes.
- `GET /episodes/<id>`: Retrieve a specific episode by ID.
- `POST /episodes`: Create a new episode.
- `PUT /episodes/<id>`: Update an existing episode.
- `PATCH /episodes/<id>`: Partially update an episode.
- `DELETE /episodes/<id>`: Delete an episode.

### Guests
- `GET /guests`: Retrieve all guests.
- `GET /guests/<id>`: Retrieve a specific guest by ID.
- `POST /guests`: Create a new guest.
- `PUT /guests/<id>`: Update an existing guest.
- `PATCH /guests/<id>`: Partially update a guest.
- `DELETE /guests/<id>`: Delete a guest.

### Appearances
- `GET /appearances`: Retrieve all appearances.
- `GET /appearances/<id>`: Retrieve a specific appearance by ID.
- `POST /appearances`: Create a new appearance.
- `PUT /appearances/<id>`: Update an existing appearance.
- `PATCH /appearances/<id>`: Partially update an appearance.
- `DELETE /appearances/<id>`: Delete an appearance.

## Configuration

The application uses a SQLite database by default. You can configure the database URI in `app/config.py`:
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///instances/lateShowDb.sqlite3'
```

## Database Migrations

To manage database schema changes, use Flask-Migrate:
- Create a new migration:
  ```bash
  flask db migrate -m "Migration message"
  ```
- Apply migrations:
  ```bash
  flask db upgrade
  ```

## Seeding the Database

To populate the database with sample data, run:
```bash
python seed.py
```

## Dependencies

- **Flask**: Web framework.
- **Flask-SQLAlchemy**: ORM for database interactions.
- **Flask-Migrate**: Database migrations.
- **Flask-RESTful**: RESTful API support.
- **SQLAlchemy-Serializer**: Serialization for models.
- **Faker**: Generate fake data for seeding.

## Development

To contribute to this project:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Faker](https://faker.readthedo


Email me: jeyceejeyka635@gmail.com