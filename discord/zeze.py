from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

# Load environment variables
load_dotenv()

# Bot token for Zeze from the environment file
TOKEN = os.getenv("DISCORD_TOKEN_ZEZE")
print(f"Loaded Token: {TOKEN}")  # Debugging line

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN_ZEZE is not set in the environment.")

# Set up intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

# Set the command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Channel ID for the #announcement channel
ANNOUNCEMENT_CHANNEL_ID = 1288274033154199594

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    # Set the bot's activity to "Watching"
    activity = discord.Activity(type=discord.ActivityType.watching, name="over the server")
    await bot.change_presence(activity=activity)

@bot.command(name='announce')
@commands.has_permissions(administrator=True)
async def announce(ctx, *, message: str):
    """Command to send an announcement to the #announcement channel."""
    channel = bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)
    if channel:
        await channel.send(message)
        await ctx.send(f'Announcement sent to {channel.mention}')
    else:
        await ctx.send('Announcement channel not found.')

# Start the bot
bot.run(TOKEN)
