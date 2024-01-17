from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

#heropowermodel
class HeroPower(db.Model):
    __tablename__ = "heros_powers"
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))

