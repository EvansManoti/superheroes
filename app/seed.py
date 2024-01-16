from app import app,db
from models import Hero

def seed_heros():
  with app.content():
    hero=Hero(name='Leo',super_name='belligoal')
    db.session.add(hero)
    db.session.commit()
