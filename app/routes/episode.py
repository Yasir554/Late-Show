from flask_restful import Resource, request
from app.models.episode import Episode
from app.extensions import db

class EpisodeResource(Resource):
    def get(self, id=None):
        """Fetch all episodes or a specific episode by ID."""
        if id is None:
            episodes = Episode.query.all()
            return [episode.to_dict() for episode in episodes], 200
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        return episode.to_dict(), 200

    def post(self):
        """Create a new episode."""
        data = request.get_json()
        date = data.get("date")
        number = data.get("number")

        episode = Episode(date=date, number=number)
        db.session.add(episode)
        db.session.commit()

        return episode.to_dict(), 201

    def put(self, id):
        """Update an existing episode."""
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404

        data = request.get_json()
        episode.date = data.get("date", episode.date)
        episode.number = data.get("number", episode.number)
        db.session.commit()

        return episode.to_dict(), 200

    def patch(self, id):
        """Partially update an existing episode."""
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404

        data = request.get_json()
        if "date" in data:
            episode.date = data["date"]
        if "number" in data:
            episode.number = data["number"]

        db.session.commit()
        return episode.to_dict(), 200

    def delete(self, id):
        """Delete an episode."""
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404

        db.session.delete(episode)
        db.session.commit()

        return {"message": "Episode deleted successfully"}, 200