import discord
from discord.ext import commands

# Your bot token (make sure to keep this private)
TOKEN = 'YOU_TOKEN_HERE'

# Enable both member and message content intents
intents = discord.Intents.default()
intents.members = True  # To track members
intents.message_content = True  # To listen to message content and commands

# Define the bot with a command prefix and the appropriate intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Respond when someone with the Members role mentions the bot (@Chomper)
@bot.event
async def on_message(message):
    # Make sure the bot doesn't respond to its own messages
    if message.author == bot.user:
        return

    # Check if the bot is mentioned and if the author has the Members role
    if bot.user in message.mentions:
        # Find the "Members" role in the guild
        members_role = discord.utils.get(message.guild.roles, name="Members")

        # Check if the author has the "Members" role
        if members_role in message.author.roles:
            await message.channel.send("You're trying to talk to a bot, go touch grass.")

    # Process commands as well
    await bot.process_commands(message)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(TOKEN)
