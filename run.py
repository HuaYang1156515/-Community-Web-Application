from app import create_app, db
from app.models import User, Event

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Add sample events if they don't exist
        if not Event.query.first():
            event1 = Event(title='Community Meeting', description='Discuss community plans and activities.', date=datetime(2024, 8, 20, 18, 0))
            event2 = Event(title='Yoga Class', description='A relaxing yoga session for all levels.', date=datetime(2024, 8, 21, 10, 0))
            db.session.add(event1)
            db.session.add(event2)
            db.session.commit()

    app.run(debug=True)
