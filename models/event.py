from app import db

class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, nullable=True)
    admin_id = db.Column(db.Integer, nullable=True)
    user_name = db.Column(db.String(50), nullable=True)
    admin_name = db.Column(db.String(50), nullable=True)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(2), default='1', nullable=False)
