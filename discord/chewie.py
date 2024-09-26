import discord
from discord.ext import commands

# Your bot token (make sure to keep this private)
TOKEN = 'YOUR_TOKEN_HERE'

# Enable both member and message content intents
intents = discord.Intents.default()
intents.members = True  # To track members
intents.message_content = True  # To listen to message content and commands

# Define the bot with a command prefix and the appropriate intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    # Set the bot's activity to "Watching"
    activity = discord.Activity(type=discord.ActivityType.watching, name="over the server")
    await bot.change_presence(activity=activity)

@bot.event
async def on_member_join(member):
    # The role name to assign (must match the exact name in your server)
    role_name = "Members"  # This is the role you want to assign to all new members

    # Find the role in the guild by name
    guild = member.guild
    role = discord.utils.get(guild.roles, name=role_name)

    if role:
        try:
            # Assign the role to the new member
            await member.add_roles(role)
            print(f"Assigned {role_name} role to {member.name}")
        except discord.Forbidden:
            print(f"Failed to assign role to {member.name}. Check bot permissions.")
        except discord.HTTPException as error:
            print(f"HTTP Exception: {error}")
    else:
        print(f"Role '{role_name}' not found in the server.")

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
            await message.channel.send("Bark bark, stupid. I'm a fucking bot.")

    # Process commands as well
    await bot.process_commands(message)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(TOKEN)
