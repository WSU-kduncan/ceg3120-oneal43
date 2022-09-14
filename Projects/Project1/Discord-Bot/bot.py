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

    smeagol_quotes = [
        'My precious.',
        'Curse the Baggins! It’s gone! What has it got in its pocketses? Oh we guess, we guess, my precious. He’s found it, yes he must have.',
        'Smeagol will swear on the Precious.',
        'It came to me. It’s mine, my own, my love, my precious.',
    ]
    if message.content == 'ring!':
    #if message.content.startswith('$ring'):
        response = random.choice(smeagol_quotes)
        await message.channel.send(response)

client.run(TOKEN)


