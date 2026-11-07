# main.py

from ai import generate_ai_response

player = {
    "name": "Player",
    "hp": 20,
    "inventory": ["broken dagger"]
}

world = {
    "location": "forest",
    "npc": {
        "goblin": {"hp": 10, "mood": "hostile"}
    }
}

def game_loop():
    print("Welcome to the game!")
    print("You are standing in a forest. Nearby, a goblin watches you.")
    print("What will you do?")

    while True:
        action = input("> ")

        if action.lower() in ["quit", "exit"]:
            print("Goodbye.")
            break
    
        ai_output = generate_ai_response(world, player, action)
        print(ai_output)


game_loop()