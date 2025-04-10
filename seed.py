from faker import Faker
from app import create_app  # Import the app factory
from app.extensions import db
from app.models.episode import Episode
from app.models.guest import Guest
from app.models.appearance import Appearance

fake = Faker()

def seed_data():
    db.session.query(Appearance).delete()
    db.session.query(Episode).delete()
    db.session.query(Guest).delete()

    episodes = [Episode(date=fake.date_this_decade(), number=fake.random_int(1, 100)) for _ in range(10)]
    guests = [Guest(name=fake.name(), occupation=fake.job()) for _ in range(15)]

    db.session.add_all(episodes + guests)
    db.session.commit()

    appearances = [
        Appearance(
            rating=fake.random_int(1, 5),
            episode_id=fake.random_element(episodes).id,
            guest_id=fake.random_element(guests).id
        )
        for _ in range(30)
    ]
    db.session.add_all(appearances)
    db.session.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    app = create_app()  # Create the Flask app
    with app.app_context():  # Push the application context
        seed_data()