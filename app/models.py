from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Hero model
class Hero(db.Model):
    __tablename__ = "heroes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hero_name = db.Column(db.String(100), nullable=False)

# Power model .
class Power(db.Model):
    __tablename__ = "powers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

# HeroPower model.
class HeroPower(db.Model):
    __tablename__ = "heroes_powers"
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))
