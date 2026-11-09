# ai.py

from openai import OpenAI

client = OpenAI()

# Prompt for AI Dungeon Master
SYSTEM_PROMPT = """You are the Dungeon Master of a text adventure game
Narrate briefly what happens after each player action.
Stay consistent with earlier events in the conversation.
Take the player's race, size, and racial traits into account: describe scenes,
obstacles, NPC reactions, and the outcome of actions accordingly
(e.g. a short character can't reach high places, a character with night vision 
sees better in caves and at night, NPCs may react to the player's race).
Do NOT let the player perform actions beyond their means.
Do NOT change the world state yourself; the game engine handles that.
Do NOT kill the player unless their HP is 0."""

MAX_HISTORY_MESSAGES = 20 # keeps token usage under control


def generate_ai_response(world, player, action, history):
    state = (
        f"Current world state: {world}\n\n"
        f"Player character:\n{player.describe_for_ai()}"
    )
        

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "system", "content": state},
        *history[-MAX_HISTORY_MESSAGES:],
        {"role": "user", "content": action},
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content