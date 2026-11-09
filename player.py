# player.py

import random

RACES = {
    "human" : {
        "stat_mods": {},
        "appearance": {},
        "traits": [

        ],
    },
    "elf": {
        "stat_mods": {},
                "appearance": {},
                "traits": [
                    
                ],
    },
    "dark_elf": {
            "stat_mods": {},
                    "appearance": {},
                    "traits": [
                        
                    ],
        },
    "dwarf": {
        "stat_mods": {},
                "appearance": {},
                "traits": [
                    
                ],
    },
    "orc": {
        "stat_mods": {},
                "appearance": {},
                "traits": [
                    
                ],
    },
    "kobold": {
        "stat_mods": {},
                "appearance": {},
                "traits": [
                    
                ],
    },
    "vampire": {
        "stat_mods": {},
                "appearance": {},
                "traits": [
                    
                ],
    },
    "demon": {
        "stat_mods": {},
                "appearance": {},
                "traits": [
                    
                ],
    },

}

BASE_STATS = {"max_hp": 20, "strength": 10, "dexterity": 10, "intelligence": 10, "charisma": 10}

class Player:
    def __init__(self, name="Player", race=None):
        self.name = name
        self.race = race or random.choice(list(RACES))
        race_data = RACES[self.race]

        self.stats = {
            stat: base + race_data["stat_mods"].get(stat, 0)
            for stat, base in BASE_STATS.items()
        }
        self.hp = self.stats["max_hp"]
        self.inventory = ["broken dagger"]

    @property
    def max_hp(self):
        return self.stats["max_hp"]

    def to_dict(self):
        return {
            "name": self.name,
            "race": self.race,
            "stats": self.stats,
            "hp": self.hp,
            "inventory": self.inventory
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(name = data["name"], race = data["race"])
        player.stats = data["stats"]
        player.hp = data["hp"]
        player.inventory = data["inventory"]
        return player

    def describe_for_ai(self):
        """Text block for AI, including race traits."""
        race_data = RACES[self.race]
        traits = "\n".join(f"- {t}" for t in race_data["traits"])
        return (
            f"Name: {self.name}\n"
            f"Race: {self.race} ({race_data['appearance']})\n"
            f"HP: {self.hp}/{self.max_hp}\n"
            f"Stats: {self.stats}\n"
            f"Inventory: {self.inventory}\n"
            f"Racial traits:\n{traits}"
        )