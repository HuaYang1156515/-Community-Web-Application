from flask import render_template
from . import main
from app.models import Event

@main.route('/')
def index():
    events = Event.query.order_by(Event.date).all()
    return render_template('main/index.html', events=events)
