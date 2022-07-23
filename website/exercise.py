from datetime import datetime
from flask import Blueprint, request
from .models import Exercise
from . import db
from sqlalchemy.sql import  extract, func
import requests


exercise = Blueprint('exercise', __name__)

@exercise.route('/exercise_add', methods=['POST'])
def add_exercise():
    if request.method == 'POST':
        exerciseName = request.form.get('exerciseName')
        hours = request.form.get('hours')
        mins = request.form.get('mins')
        db.session.add(Exercise(exercise_name=exerciseName, hours= hours, mins= mins))
        db.session.commit()
    return "<h1>Added successfully To the database</h1>"

@exercise.route('/retrieve_month')
def retrieve_month():
    current_month = Exercise.query.filter(extract('month',Exercise.date) == datetime.now().month, 
    extract('year',Exercise.date) == datetime.now().year ).all()
    return f"<h1>The number of enters in this month is {len(current_month)}</h1>"

@exercise.route('/highest_month')
def highest_month():
    highest_mon_entires = db.session.query(extract('month',Exercise.date).label('month')
    ,func.count(Exercise.id).label('count')).filter(extract('year',Exercise.date) == datetime.now().year).order_by(
        func.count(Exercise.id).label('count').desc()).group_by(extract('month',Exercise.date)).first()


    return f"<h1> The month which has the highest enters is {highest_mon_entires.month} and the number of enters is {highest_mon_entires.count}"

@exercise.route('/test_add_exercises')
def month():
    route_answer =  requests.post("http://127.0.0.1:5000/exercise_add", data  = {'exerciseName':'Football', 'hours':1, 'mins':30})
    return route_answer.text
