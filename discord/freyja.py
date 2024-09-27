from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import openai
import asyncio

# Load environment variables
load_dotenv()

# Set your OpenAI API key and Discord token from the environment file
openai.api_key = os.getenv('OPENAI_API_KEY')
TOKEN = os.getenv("DISCORD_TOKEN_FREYJA")

# Check if the tokens were loaded correctly
if not openai.api_key:
    raise ValueError("OpenAI API key is missing in the environment variables.")

if not TOKEN:  # Corrected from DISCORD_TOKEN to TOKEN
    raise ValueError("Discord token is missing in the environment variables.")

# Set up intents (required for Discord bot)
intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True  # Enable DM intents

# Create a bot instance with '.' as the command prefix
bot = commands.Bot(command_prefix='.', intents=intents)

# Dictionary to track users who received the welcome message
user_welcome_status = {}

# Function to handle rate-limiting (retry after waiting)
async def handle_rate_limiting(retry_after):
    print(f"Rate limit hit. Retrying in {retry_after:.2f} seconds...")
    await asyncio.sleep(retry_after)  # Sleep for the retry_after duration

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    # Set the bot's activity to "Watching"
    activity = discord.Activity(type=discord.ActivityType.watching, name="over the server")
    await bot.change_presence(activity=activity)

# Helper function to split long messages
def split_message(text, limit=2000):
    """Split a long message into chunks of 'limit' characters."""
    return [text[i:i+limit] for i in range(0, len(text), limit)]

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message is from a DM
    if isinstance(message.channel, discord.DMChannel):
        # Send a welcome message to new users who have not received it before
        if message.author.id not in user_welcome_status:
            welcome_message = (
                "Hello! Thank you for messaging me. Here's how you can interact with me:\n"
                "- Use the `.ai <your question>` command to ask me anything.\n"
                "- I will respond directly to your DMs!\n"
                "If you need any help, just let me know!"
            )
            await message.author.send(welcome_message)
            # Mark this user as having received the welcome message
            user_welcome_status[message.author.id] = True

        # Handle the AI response if the user sends a message in DM
        if message.content.startswith('.ai'):
            user_message = message.content[len('.ai '):].strip()
            if not user_message:
                await message.channel.send("Error: No message provided for the AI to respond to.")
                return
            try:
                retries = 0  # Retry counter
                max_retries = 5  # Maximum retries to avoid infinite loop
                while retries < max_retries:
                    try:
                        response = openai.ChatCompletion.create(
                            model="gpt-4o-2024-08-06",  # Updated model version
                            messages=[
                                {"role": "system", "content": "You are a helpful assistant."},
                                {"role": "user", "content": user_message}
                            ],
                            max_tokens=1500  # Set max tokens for the response
                        )

                        # Extract the response text
                        response_text = response['choices'][0]['message']['content'].strip()

                        # Split the message into chunks if it's longer than 2000 characters
                        response_chunks = split_message(response_text)

                        # Send the AI's response to the user in DM
                        for chunk in response_chunks:
                            await message.author.send(chunk)
                        break  # Exit loop on success

                    except openai.error.RateLimitError as e:
                        retry_after = float(e.headers.get('Retry-After', 1))  # Get suggested retry time
                        await handle_rate_limiting(retry_after)
                        retries += 1

            except Exception as e:
                await message.author.send(f"Error: {str(e)}")
        else:
            # Handle generic DM responses
            await message.author.send("Thanks for messaging me directly! How can I assist you?")

        # Don't let the bot continue processing this as a normal server message
        return

    # Else, the message was sent in a guild channel
    # Handle messages sent in a guild channel

    # Find the #ai channel
    ai_channel = discord.utils.get(message.guild.channels, name='ai')

    if not ai_channel:
        await message.channel.send("Error: I couldn't find the #ai channel.")
        return

    # Handle the .ai command in the guild (server) channel
    if message.content.startswith('.ai'):
        user_message = message.content[len('.ai '):].strip()
        if not user_message:  # Check for empty or invalid user message
            await message.channel.send("Error: No message provided for the AI to respond to.")
            return
        try:
            retries = 0  # Retry counter
            max_retries = 5  # Maximum retries to avoid infinite loop
            while retries < max_retries:
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4o-2024-08-06",  # Updated model version
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": user_message}
                        ],
                        max_tokens=1500  # Set max tokens for the response
                    )

                    # Extract the response text
                    response_text = response['choices'][0]['message']['content'].strip()

                    # Split the message into chunks if it's longer than 2000 characters
                    response_chunks = split_message(response_text)

                    # Send the AI's response in a DM instead of the #ai channel
                    for chunk in response_chunks:
                        await message.author.send(chunk)  # Send DM to the message author
                    break  # Exit loop on success

                except openai.error.RateLimitError as e:
                    retry_after = float(e.headers.get('Retry-After', 1))  # Get suggested retry time
                    await handle_rate_limiting(retry_after)
                    retries += 1

        except Exception as e:
            await message.author.send(f"Error: {str(e)}")  # Send error in DM instead of channel

    # Handle the .id_model command in guild (server) channel
    elif message.content.startswith('.id_model'):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-2024-08-06",  # Updated model version
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Can you tell me which model you are?"}
                ],
                max_tokens=10
            )

            # Log the model used and send the model name as a message
            model_used = response['model']
            await message.author.send(f"I'm currently using the model: {model_used}")  # Send in DM

        except Exception as e:
            await message.author.send(f"Error: {str(e)}")  # Send error in DM

    # Ensure other commands and events still work
    await bot.process_commands(message)

# Run the bot
bot.run(TOKEN)  # Changed this to TOKEN
