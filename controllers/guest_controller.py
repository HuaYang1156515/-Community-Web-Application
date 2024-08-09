from flask import Blueprint, render_template
from services.event_service import get_event_by_id

guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route('/')
def home():
    return render_template('home.html')

@guest_bp.route('/event/<int:event_id>', methods=['GET'])
def event_detail(event_id):
    event = get_event_by_id(event_id)
    if event:
        return render_template('event_detail.html', event=event)
    return "Event not found", 404
