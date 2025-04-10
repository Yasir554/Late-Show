from flask_restful import Resource, request
from app.models.appearance import Appearance
from app.models.episode import Episode
from app.models.guest import Guest
from app.extensions import db

class AppearanceResource(Resource):
    def get(self, id=None):
        """Fetch all appearances or a specific appearance by ID."""
        if id is None:
            appearances = Appearance.query.all()
            return [appearance.to_dict() for appearance in appearances], 200
        appearance = Appearance.query.get(id)
        if not appearance:
            return {"error": "Appearance not found"}, 404
        return appearance.to_dict(), 200

    def post(self):
        """Create a new appearance."""
        data = request.get_json()
        rating = data.get("rating")
        episode_id = data.get("episode_id")
        guest_id = data.get("guest_id")

        if not (1 <= rating <= 5):
            return {"errors": ["Rating must be between 1 and 5"]}, 422

        episode = Episode.query.get(episode_id)
        guest = Guest.query.get(guest_id)
        if not episode or not guest:
            return {"errors": ["Invalid episode or guest ID"]}, 422

        appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
        db.session.add(appearance)
        db.session.commit()

        return appearance.to_dict(), 201

    def put(self, id):
        """Update an existing appearance."""
        appearance = Appearance.query.get(id)
        if not appearance:
            return {"error": "Appearance not found"}, 404

        data = request.get_json()
        appearance.rating = data.get("rating", appearance.rating)
        db.session.commit()

        return appearance.to_dict(), 200

    def patch(self, id):
        """Partially update an existing appearance."""
        appearance = Appearance.query.get(id)
        if not appearance:
            return {"error": "Appearance not found"}, 404

        data = request.get_json()
        if "rating" in data:
            appearance.rating = data["rating"]
        if "episode_id" in data:
            appearance.episode_id = data["episode_id"]
        if "guest_id" in data:
            appearance.guest_id = data["guest_id"]

        db.session.commit()
        return appearance.to_dict(), 200

    def delete(self, id):
        """Delete an appearance."""
        appearance = Appearance.query.get(id)
        if not appearance:
            return {"error": "Appearance not found"}, 404

        db.session.delete(appearance)
        db.session.commit()

        return {"message": "Appearance deleted successfully"}, 200