import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def process_message(content):
    # Si le message est uniquement "6"
    if content.strip() == "6":
        return "7 !"

def process_message(content):
    # Si le message est uniquement "6"
    if content.strip() == "six":
        return "Seven !"

def process_message(content):
    # Si le message est uniquement "6"
    if content.strip() == "Six":
        return "Seven !"
    
    # Sinon, on barre tout sauf les "6"
    result = ""
    for char in content:
        if char == "6":
            result += "6"
        elif char.strip() == "":
            result += char  # garder les espaces
        else:
            result += f"~~{char}~~"
    
    return f"{result}\n7 !"

    result = ""
    for char in content:
        if char == "Six":
            result += "Six"
        elif char.strip() == "":
            result += char  # garder les espaces
        else:
            result += f"~~{char}~~"
    
    return f"{result}\nSeven !"

    result = ""
    for char in content:
        if char == "six":
            result += "six"
        elif char.strip() == "":
            result += char  # garder les espaces
        else:
            result += f"~~{char}~~"
    
    return f"{result}\nSeven !"

@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "6" in message.content:
        response = process_message(message.content)
        await message.reply(response)

    if "Six" in message.content:
        response = process_message(message.content)
        await message.reply(response)

    if "six" in message.content:
        response = process_message(message.content)
        await message.reply(response)

TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
