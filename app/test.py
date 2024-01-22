import os

abs_path=os.getcwd()

print(abs_path)

print(os.path.normpath(abs_path))


#names of heroes
hero_names = [
    {"id": 1, "name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"id": 2, "name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"id": 3, "name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"id": 4, "name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"id": 5, "name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"id": 6, "name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"id": 7, "name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"id": 8, "name": "Ororo Munroe", "super_name": "Storm"},
    {"id": 9, "name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"id": 10, "name": "Elektra Natchios", "super_name": "Elektra"},
]

#powername and description
powers_data = [
    {
        "id": 1,
        "name": "super strength",
        "description": "gives the wielder super-human strengths",
    },
    {
        "id": 2,
        "name": "flight",
        "description": "gives the wielder the ability to fly through the skies at supersonic speed",
    },
    {
        "id": 3,
        "name": "super human senses",
        "description": "allows the wielder to use her senses at a super-human level",
    },
    {
        "id": 4,
        "name": "elasticity",
        "description": "can stretch the human body to extreme lengths",
    },
]

#power data of heroes
heros_powers_data = [
    {"hero_id": 1, "power_id": 1},  # hero one & power
    {"hero_id": 2, "power_id": 2},  # hero two & power
    {"hero_id": 3, "power_id": 3},  # hero three & power
    {"hero_id": 4, "power_id": 4},  # hero four & power
    {"hero_id": 5, "power_id": 1},  # hero five & power
    {"hero_id": 6, "power_id": 2},  # hero six & power
    {"hero_id": 7, "power_id": 3},  # hero seven & power
    {"hero_id": 8, "power_id": 4},  # hero eigth & power
    {"hero_id": 9, "power_id": 1},  # hero nine & power
    {"hero_id": 10, "power_id": 2},  # hero ten & power
]