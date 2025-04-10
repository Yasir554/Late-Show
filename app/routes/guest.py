from flask_restful import Resource, request
from app.models.guest import Guest
from app.extensions import db

class GuestResource(Resource):
    def get(self, id=None):
        """Fetch all guests or a specific guest by ID."""
        if id is None:
            guests = Guest.query.all()
            return [guest.to_dict() for guest in guests], 200
        guest = Guest.query.get(id)
        if not guest:
            return {"error": "Guest not found"}, 404
        return guest.to_dict(), 200

    def post(self):
        """Create a new guest."""
        data = request.get_json()
        name = data.get("name")
        occupation = data.get("occupation")

        guest = Guest(name=name, occupation=occupation)
        db.session.add(guest)
        db.session.commit()

        return guest.to_dict(), 201

    def put(self, id):
        """Update an existing guest."""
        guest = Guest.query.get(id)
        if not guest:
            return {"error": "Guest not found"}, 404

        data = request.get_json()
        guest.name = data.get("name", guest.name)
        guest.occupation = data.get("occupation", guest.occupation)
        db.session.commit()

        return guest.to_dict(), 200

    def patch(self, id):
        """Partially update an existing guest."""
        guest = Guest.query.get(id)
        if not guest:
            return {"error": "Guest not found"}, 404

        data = request.get_json()
        if "name" in data:
            guest.name = data["name"]
        if "occupation" in data:
            guest.occupation = data["occupation"]

        db.session.commit()
        return guest.to_dict(), 200

    def delete(self, id):
        """Delete a guest."""
        guest = Guest.query.get(id)
        if not guest:
            return {"error": "Guest not found"}, 404

        db.session.delete(guest)
        db.session.commit()

        return {"message": "Guest deleted successfully"}, 200