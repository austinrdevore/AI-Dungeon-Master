# ai.py

from openai import OpenAI

client = OpenAI()

# Prompt for AI Dungeon Master
SYSTEM_PROMPT = """You are the Dungeon Master of a text adventure game
Narrate briefly what happens after each player action.
Stay consistent with earlier events in the conversation.
Do NOT change the world state yourself; the game engine handles that.
Do NOT kill the player unless their HP is 0."""

MAX_HISTORY_MESSAGES = 20 # keeps token usage under control


def generate_ai_response(world, player, action, history):
    state = f"Current world state: {world}\nCurrent player state: {player}"

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