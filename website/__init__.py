from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import urandom

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    fsk_secret_key = urandom(12)
    conn = 'mysql+pymysql://root:@localhost/tourism'

    app.config['SECRET_KEY'] = fsk_secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = conn
    db.init_app(app)


    from .exercise import exercise

    app.register_blueprint(exercise, url_prefix='/')
    db.create_all(app=app)

    return app



    
        
