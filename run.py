from app import create_app, db
from app.models import User, Event

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# Create database tables
with app.app_context():
    db.create_all()
