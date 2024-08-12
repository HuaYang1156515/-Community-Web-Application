from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'   

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    login = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    
    status = db.Column(db.String(2), default='1', nullable=False)
    pic = db.Column(db.String(255), nullable=True)
    desc = db.Column(db.String(255), nullable=True)

"""
    def set_password(self, password):
         
        self.password = generate_password_hash(password)

    def check_password(self, password):
         
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.login}>'
"""