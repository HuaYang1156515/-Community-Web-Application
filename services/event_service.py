from models.event import Event
from app import db

def get_event_by_id(event_id):
    return Event.query.filter_by(id=event_id).first()

def create_event(active_name, active_time, active_location, active_desc, user_id=None, admin_id=None):
    new_event = Event(active_name=active_name, active_time=active_time, active_location=active_location, active_desc=active_desc, user_id=user_id, admin_id=admin_id)
    db.session.add(new_event)
    db.session.commit()
    return new_event
