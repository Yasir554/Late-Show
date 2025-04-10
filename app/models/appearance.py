from app.extensions import db
from sqlalchemy_serializer import SerializerMixin

class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    # Exclude episode and guest to avoid circular references
    serialize_rules = ('-episode', '-guest')