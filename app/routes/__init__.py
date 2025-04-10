from .episode import EpisodeResource
from .guest import GuestResource
from .appearance import AppearanceResource

def register_routes(api):
    api.add_resource(EpisodeResource, '/episodes', '/episodes/<int:id>')
    api.add_resource(GuestResource, '/guests', '/guests/<int:id>')
    api.add_resource(AppearanceResource, '/appearances', '/appearances/<int:id>')