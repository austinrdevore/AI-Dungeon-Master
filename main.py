# main.py

from ai import generate_ai_response
from engine import save_game, load_game
from player import Player


DEFAULT_WORLD = {
    "location": "forest",
    "npc": {
        "goblin": {"hp": 10, "mood": "hostile"}
    }
}

def game_loop():
    player = Player()
    world = {**DEFAULT_WORLD}
    history = []

    saved = load_game()
    if saved:
        choice = input("Saved game found. Load it? (y/n): ").strip().lower()
        if choice == "y":
            world, history = saved["world"], saved["history"]
            player = Player.from_dict(saved["player"])
            print("Game loaded successfully.")
            if history:
                print("Previously:")
                print(history[-1]["content"])
    if not history:
        print(f"Welcome to the game! You are a {player.race}!")
        print("During any turn, type 'save' to save your game, or 'quit' to quit the game.")
        print("You are standing in a forest. Nearby, a goblin watches you.")
    print("What will you do?")

    while True:
        action = input("> ").strip()

        if action.lower() in ["quit", "exit"]:
            print("Goodbye.")
            break

        if action.lower() == "save":
            save_game(world, player.to_dict(), history)
            print("Game saved.")
            continue
    
        ai_output = generate_ai_response(world, player, action, history)
        print(ai_output)

        history.append({"role": "user", "content": action})
        history.append({"role": "assistant", "content": ai_output})

if __name__ == "__main__":
    game_loop()