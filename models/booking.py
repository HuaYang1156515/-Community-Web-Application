from app import db

class ActiveUser(db.Model):
    __tablename__ = 'web_active_user'
    id = db.Column(db.Integer, primary_key=True)
    active_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(2), default='1', nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(2), nullable=True)
