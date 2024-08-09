from models.user import User
from app import db

def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()

def create_user(name, login, password):
    new_user = User(name=name, login=login, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user
