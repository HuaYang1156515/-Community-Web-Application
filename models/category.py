from app import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(2), default='1', nullable=False)

    def __repr__(self):
        return f'<Category {self.name}>'
