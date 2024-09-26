import discord
from discord.ext import commands
import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_KEY'  # Make sure this is correctly set

# Directly set your Discord token
DISCORD_TOKEN = 'YOUR_TOKEN_HERE'

# Set up intents (required for Discord bot)
intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance with '.' as the command prefix
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Find the #ai channel
    ai_channel = discord.utils.get(message.guild.channels, name='ai')

    if not ai_channel:
        await message.channel.send("Error: I couldn't find the #ai channel.")
        return

    # Handle the .ai command
    if message.content.startswith('.ai'):
        user_message = message.content[len('.ai '):].strip()
        if not user_message:  # Check for empty or invalid user message
            await message.channel.send("Error: No message provided for the AI to respond to.")
            return
        try:
            # Use ChatCompletion for the correct model (gpt-4o as you specified)
            response = openai.ChatCompletion.create(
                model="gpt-4o",  # Your tested model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=3000  # Adjusted max token limit to avoid error
            )

            # Extract the response text
            response_text = response['choices'][0]['message']['content'].strip()

            # Send the AI's response to the #ai channel
            await ai_channel.send(response_text)

        except Exception as e:
            await ai_channel.send(f"Error: {str(e)}")

    # Handle the .id_model command
    elif message.content.startswith('.id_model'):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",  # Your tested model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Can you tell me which model you are?"}
                ],
                max_tokens=10
            )

            # Log the model used and send the model name as a message
            model_used = response['model']
            await ai_channel.send(f"I'm currently using the model: {model_used}")

        except Exception as e:
            await ai_channel.send(f"Error: {str(e)}")

    # Ensure other commands and events still work
    await bot.process_commands(message)

# Run the bot
bot.run(DISCORD_TOKEN)
