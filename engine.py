# engine.py

import json
import os

SAVE_FILE = "savegame.json"


def save_game(world, player, history, path=SAVE_FILE):
    data = {"world": world, "player": player, "history": history}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_game(path=SAVE_FILE):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)