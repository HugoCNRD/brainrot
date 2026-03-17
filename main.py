import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def process_message(content):
    content_clean = content.strip()

    # Direct responses
    if content_clean.lower() == "6":
        return "7 !"
    if content_clean.lower() == "six":
        return "Seven !"
    if content_clean == "Six":  # cas spécial majuscules
        return "Seven !"

    # Otherwise strike everything except "6"
    result = ""
    for char in content:
        if char == "6":
            result += "6"
        elif char.strip() == "":
            result += char
        else:
            result += f"~~{char}~~"

    return f"{result}\n7 !"


@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

   
    if message.content.startswith("http"):
        return

    
    if message.content.startswith("<@"):
        return

    if any(x in message.content for x in ["6", "Six", "six", "SIX"]):
        response = process_message(message.content)
        await message.reply(response)


TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)