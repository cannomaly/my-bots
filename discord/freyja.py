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

    # Command to trigger the AI conversation (e.g., .ai)
    if message.content.startswith('.ai'):
        ai_channel = discord.utils.get(message.guild.channels, name='ai')

        if ai_channel:
            user_message = message.content[len('.ai '):]
            try:
                # Use ChatCompletion for chat-based models (gpt-3.5-turbo or gpt-4)
                response = openai.ChatCompletion.create(
                    model="gpt-4o",  # You can also use "gpt-4" if available
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_message}
                    ],
                    max_tokens=150  # Limit the response length
                )

                # Extract the response text
                response_text = response['choices'][0]['message']['content'].strip()

                # Send the AI's response to the #ai channel
                await ai_channel.send(response_text)

            except Exception as e:
                await ai_channel.send(f"Error: {str(e)}")
        else:
            await message.channel.send("Error: I couldn't find the #ai channel.")

    # Ensure other commands and events still work
    await bot.process_commands(message)

@bot.command(name='identify_model')
async def id_model(ctx):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Use GPT-4 here
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": "Can you tell me which model you are?"}],
            max_tokens=10
        )

        # Log the model used and send the model name as a message
        model_used = response['model']
        await ctx.send(f"I'm currently using the model: {model_used}")

    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Run the bot
bot.run(DISCORD_TOKEN)
