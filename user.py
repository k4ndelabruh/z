from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship with freight requests
    requests = db.relationship('FreightRequest', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')" 