from app import db

class Event(db.Model):
    __tablename__ = 'web_active'
    id = db.Column(db.Integer, primary_key=True)
    active_name = db.Column(db.String(50), nullable=False)
    active_time = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, nullable=True)
    admin_id = db.Column(db.Integer, nullable=True)
    user_name = db.Column(db.String(50), nullable=True)
    admin_name = db.Column(db.String(50), nullable=True)
    active_location = db.Column(db.String(255), nullable=False)
    active_desc = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(2), default='1', nullable=False)
