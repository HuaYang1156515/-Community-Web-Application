from flask import Blueprint, render_template
from app.models import Event

main = Blueprint('main', __name__)

@main.route('/')
def index():
    events = Event.query.order_by(Event.date).all()
    return render_template('main/index.html', events=events)
