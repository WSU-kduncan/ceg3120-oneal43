import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('CEG3120-Project1')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    LoTR_quotes = [
        'But in the end it’s only a passing thing, this shadow; even darkness must pass.',
        'It’s a dangerous business, Frodo, going out your door. You step onto the road, and if you don’t keep your feet, there’s no knowing where you might be swept off to.',
        'A wizard is never late, Frodo Baggins. Nor is he early. He arrives precisely when he means to.',
        'It came to me. It’s mine, my own, my love, my precious.',
    ]
    if message.content == 'ring!':
    #if message.content.startswith('$ring'):
        response = random.choice(LoTR_quotes)
        await message.channel.send(response)

client.run(TOKEN)

