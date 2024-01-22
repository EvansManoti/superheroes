from app import app, db
from models import Hero, Power, HeroPower

#heroes
allHeros = [
    { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
    { "name": "Doreen Green", "super_name": "Squirrel Girl" },
    { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
    { "name": "Janet Van Dyne", "super_name": "The Wasp" },
    { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
    { "name": "Carol Danvers", "super_name": "Captain Marvel" },
    { "name": "Jean Grey", "super_name": "Dark Phoenix" },
    { "name": "Ororo Munroe", "super_name": "Storm" },
    { "name": "Kitty Pryde", "super_name": "Shadowcat" },
    { "name": "Elektra Natchios", "super_name": "Elektra" }
]

def seed_hero():
    with app.app_context():
        hero = [
            Hero(name=hero["name"], super_name=hero["super_name"]) for hero in allHeros
        ]
        db.session.add(hero)
        db.session.commit()


#power
allPowers = [
    { "name": "super strength", "description": "gives the wielder super-human strengths" },
    { "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
    { "name": "super human senses", "description": "allows the wielder to use her senses at a super-human level" },
    { "name": "elasticity", "description": "can stretch the human body to extreme lengths" }
]



def seed_power():
    with app.app_context():
        power = [
            power(name=power["name"], super_strength=power["super_strength"]) for power in allPowers
        ]
        db.session.add(power)
        db.session.commit()



#strength
allStrengths = ["Strong", "Weak", "Average"]


def seed_strength():
    with app.app_context():
        strength = [
            strength(name=strength) for strength in allStrengths
        ]
        db.session.add(strength)
        db.session.commit()
