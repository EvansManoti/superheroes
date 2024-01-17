#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Hero

import os

abs_path=os.getcwd()

db_path=f'sqlite:///{abs_path}/db/app.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

# @app.route('/add-dumy')
# def add_dummy():
#     hero=Hero(name='Leo',super_name='belligoal')
#     db.session.add(hero)
#     db.session.commit()

#     return 'Hero added'

#heromodel
class Hero(db.Model):
    __tablename__ = "heroes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hero_name = db.Column(db.String(100), nullable=False)
    powers = db.Column(db.String(100), nullable=False)


#powermodel
class Power(db.model):
    __tablename__="powers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)


if __name__ == '__main__':
    app.run(port=3000,debug = True )



