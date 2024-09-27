from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import discord
from discord.ext import commands, tasks
import logging

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables
load_dotenv()

# Bot token and YouTube API key from the environment file
TOKEN = os.getenv("DISCORD_TOKEN_CHOMPER")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

if TOKEN is None or YOUTUBE_API_KEY is None:
    raise ValueError("Environment variables are not set.")

# YouTube API client setup
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Set up intents (including message content intent)
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Change the command prefix to ?
bot = commands.Bot(command_prefix='?', intents=intents)

# Channel ID for the #announcement channel
ANNOUNCEMENT_CHANNEL_ID = 1288274033154199594

# Store the last announced video ID for your YouTube channel
tracked_channel_id = 'UCQMPP0PYhvDjn_Lq6vzM7UA'  # Your YouTube channel ID
last_video_id = None

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    activity = discord.Activity(type=discord.ActivityType.watching, name="over the server")
    await bot.change_presence(activity=activity)
    check_new_videos.start()  # Start checking for new videos

# Function to fetch the latest video from a YouTube channel
async def fetch_latest_video(channel_id):
    request = youtube.activities().list(
        part="snippet,contentDetails",
        channelId=channel_id,
        maxResults=1
    )
    response = request.execute()

    if "items" in response:
        latest_video = response['items'][0]
        video_id = latest_video['contentDetails']['upload']['videoId']
        video_title = latest_video['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_id, video_title, video_url
    return None, None, None

# Task to check for new video uploads every 5 minutes
@tasks.loop(minutes=5)
async def check_new_videos():
    global last_video_id
    video_id, video_title, video_url = await fetch_latest_video(tracked_channel_id)
    if video_id and video_id != last_video_id:
        channel = bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)
        message = f"📢 **New video uploaded:** {video_title}\nWatch here: {video_url}"
        await channel.send(message)
        last_video_id = video_id  # Update last video ID

# Simple test command to check if the bot is running
@bot.command(name='ping')
async def ping(ctx):
    print("Ping command received")  # Debugging line
    await ctx.send("Pong!")

# Start the bot
bot.run(TOKEN)
