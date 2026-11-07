# ai.py

from openai import OpenAI

client = OpenAI()

def generate_ai_response(world, player, action):
    prompt = f"""
You are the Dungeon Master of a text adventure game.

Here is the current world state:
{world}

Here is the player state:
{player}

The player attempts the following action:
"{action}"

Respond with a short narration describing what happens next.
Do NOT change the world state yourself.
Do NOT kill the player unless their HP is 0.
"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content