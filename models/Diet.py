from database import db
from datetime import date


class Diet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=date.today())
    is_within_the_diet = db.Column(db.Boolean, nullable=False, default=False)
