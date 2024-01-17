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

@app.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    heroes_data = [
        {"id": hero.id, "name": hero.name, "super_name": hero.super_name}
        for hero in heroes
    ]
    return jsonify(heroes_data)



if __name__ == '__main__':
    app.run(port=3000,debug = True )



