from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

#create database
from app import db, create_app
from app.models import User

app = create_app()
app.app_context().push()
db.create_all()
