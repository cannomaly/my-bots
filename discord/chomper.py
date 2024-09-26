from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

# Load environment variables
load_dotenv()

# Bot token from the environment file
TOKEN = os.getenv("DISCORD_TOKEN_CHOMPER")

# Set up intents
intents = discord.Intents.default()
intents.members = True  # To track members
intents.message_content = True  # To listen to message content and commands

# Define the bot with a command prefix and the appropriate intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    # Set the bot's activity
    activity = discord.Activity(type=discord.ActivityType.watching, name="over the server")
    await bot.change_presence(activity=activity)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
        members_role = discord.utils.get(message.guild.roles, name="Members")

        if members_role in message.author.roles:
            await message.channel.send("You're trying to talk to a bot, go touch grass.")

    await bot.process_commands(message)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Start the bot
bot.run(TOKEN)
