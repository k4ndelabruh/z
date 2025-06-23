from app import db
from datetime import datetime

class FreightRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    transport_date = db.Column(db.DateTime, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    dimensions = db.Column(db.String(100), nullable=False)
    cargo_type = db.Column(db.String(100), nullable=False)
    pickup_address = db.Column(db.String(255), nullable=False)
    delivery_address = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), default="Новая")
    
    # Foreign key to user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"FreightRequest(ID: {self.id}, User: {self.user_id}, Type: {self.cargo_type})" 