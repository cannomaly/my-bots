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

    # Automatically assign roles to members who already exist in the server
    for guild in bot.guilds:
        await assign_roles_to_existing_members(guild)

async def assign_roles_to_existing_members(guild):
    bot_member = guild.get_member(bot.user.id)

    if bot_member.guild_permissions.manage_roles:
        for member in guild.members:
            # Skip members who already have the correct role
            if member.bot:
                role_name = "Set_Bots_Role"  # Role to assign to bots
            else:
                role_name = "Set_Members_Role"  # Role to assign to human members

            role = discord.utils.get(guild.roles, name=role_name)

            if role and role not in member.roles:
                try:
                    await member.add_roles(role)
                    print(f"Assigned {role_name} role to {member.name}")
                except discord.Forbidden:
                    print(f"Failed to assign role to {member.name}. Check bot permissions.")
                except discord.HTTPException as error:
                    print(f"HTTP Exception: {error}")
    else:
        print("Bot does not have permission to manage roles.")

@bot.event
async def on_member_join(member):
    # Ensure the bot has the required permission to manage roles
    guild = member.guild
    bot_member = guild.get_member(bot.user.id)

    if bot_member.guild_permissions.manage_roles:
        # Check if the new member is a bot or a human
        if member.bot:
            role_name = "Set_Bot_Role"  # Role to assign to bots
        else:
            role_name = "Set_Membrers_Role"  # Role to assign to human members

        role = discord.utils.get(guild.roles, name=role_name)

        if role:
            try:
                await member.add_roles(role)
                print(f"Assigned {role_name} role to {member.name}")
            except discord.Forbidden:
                print(f"Failed to assign role to {member.name}. Check bot permissions.")
            except discord.HTTPException as error:
                print(f"HTTP Exception: {error}")
        else:
            print(f"Role '{role_name}' not found in the server.")
    else:
        print("Bot does not have permission to manage roles.")

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(TOKEN)
