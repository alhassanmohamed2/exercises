from . import db
from sqlalchemy.sql import func

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String(255))
    hours = db.Column(db.Integer)  
    mins = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

