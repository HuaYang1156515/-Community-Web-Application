from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'web_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    login = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    login_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(2), default='1', nullable=False)
    pic = db.Column(db.String(255), nullable=True)
    desc = db.Column(db.String(255), nullable=True)

"""
class User(db.Model):
    __tablename__ = 'web_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    login = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    login_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(2), default='1', nullable=False)
    pic = db.Column(db.String(255), nullable=True)
    desc = db.Column(db.String(255), nullable=True)
"""