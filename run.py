from app import create_app, db
from app.models import User, Event
from datetime import datetime

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Create database tables
        db.create_all()

        # Add sample events
        if not Event.query.first():
            event1 = Event(title='Community Meeting', description='Discuss community plans and activities.', date=datetime(2024, 8, 15, 10, 0, 0))
            event2 = Event(title='Yoga Class', description='A relaxing yoga session for all levels.', date=datetime(2024, 8, 20, 17, 0, 0))
            db.session.add(event1)
            db.session.add(event2)
            db.session.commit()

    app.run(debug=True)
