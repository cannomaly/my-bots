# Discord Bots Collection

*This repository contains multiple personal Discord bots, each with a unique set of features for server administration and automation.*

## 1. Chewie - Automatic Role Assignment Bot

*Chewie is a Discord bot that automatically assigns roles to users and bots upon joining the server.*

### Features

- **Automatic Role Assignment**:  
  Chewie assigns a "Members" role to human members and a "Frenchies" role to bots upon joining the server.
  
- **Existing Member Role Assignment**:  
  When the bot starts, it checks all existing members in the server and assigns them the correct roles based on whether they are bots or humans.

- **Manage Role Permissions**:  
  The bot checks for permission to manage roles, ensuring it can assign roles properly to members.

### Commands

- No user-facing commands; the bot operates automatically upon server events.

## 2. Chomper - AI-Powered Discord Bot (Under Development)

*Chomper integrates with the OpenAI API to provide AI-generated responses through DMs. Note: This bot is still under development.*

### Features

- **AI-Generated Responses**:  
  Chomper listens to specific keywords in server channels and provides AI-generated responses in DMs using OpenAI's GPT models.

- **Rate Limit Handling**:  
  If the OpenAI API rate limit is hit, Chomper waits and retries, ensuring smooth interaction with the API.

- **Model Identification**:  
  The bot can identify which OpenAI model it is using with the `.id_model` command.

### Commands

- **.id_model**:  
  Sends a DM to the user with the model currently in use by the bot.

## 3. Freyja - OpenAI Discord Bot

*Freyja is an OpenAI Discord bot designed to handle rate-limited API requests and manage model-related interactions for OpenAI.*

### Features

- **Rate-Limit Retry**:  
  If an API request exceeds the rate limit, Freyja manages the retries based on the provided retry-after time.
  
- **Model Query Command**:  
  Freyja can respond with the OpenAI model in use when asked with the `.id_model` command.

- **Error Handling**:  
  Freyja handles errors and sends relevant information back to users via DM.

### Commands

- **.id_model**:  
  Queries the current OpenAI model in use and responds in the user’s DM.

## 4. ZeZe - Announcement Discord Bot

*ZeZe is an announcement discord bot.*

A powerful and feature-rich Discord bot tailored for server administrators to manage and send announcements in a streamlined and organized way. It includes features for scheduling announcements, urgent notifications, and logging past messages.

### Features

- **Scheduled Announcements**:  
  Use the `!schedule_announce HH:MM message` command to schedule an announcement for a specific time (24-hour format).  
  Example: `!schedule_announce 14:30 Server maintenance will start soon!` will schedule a message at 14:30.

- **Immediate Announcements**:  
  Send an instant announcement to the designated announcement channel using the `!announce message` command.  
  Example: `!announce Server update is live!` will post the announcement immediately.

- **Urgent Announcements**:  
  Use the `!urgent_announce message` command to send high-priority, urgent announcements with special formatting.  
  Example: `!urgent_announce Critical server downtime!` will send an alert with an urgent tag.

- **Announcement Logs**:  
  Keep track of all past announcements using the `!view_log` command, showing previous announcements along with their timestamps and authors.

- **View Scheduled Announcements**:  
  Admins can use the `!view_schedule` command to view all upcoming scheduled announcements.

- **Help Command**:  
  Admins can use the `!help` command to get a list of all available commands and their descriptions.

## Setup Instructions

**1. Clone the Repository**  
You will need to clone the bots repository and then change to the cloned repository so you can make the changes needed.
- Clone the bot's repository: `git clone https://github.com/cannomaly/my-bots.git`
- Change to the cloned repo `cd <bot-directory>`
- Run the command: `ls` or `ls -lh` to get a list of my discord bots.

**2. Install Dependencies**  
Make sure Python 3.8+ is installed. Set up a Python virtual environment and install the required dependencies by running the following commands:
- Create a virtual environment: `python3 -m venv venv`
- Activate the virtual environment: `source venv/bin/activate` or `.\venv/bin/activate.fish` for fish shell.
- Install dependencies: `pip install discord.py python-dotenv openai`

**3. Set Up Environment Variables**  
Create a `.env` file the root directory of the project or edit the one included in my repo.
- Run `ls -lha` to see hidden files as .env is a hidden file.
- Edit the .env file like so: `vim .env` or `nano .env`
- Add your bot token to the file like so: `DISCORD_TOKEN_<BOT_NAME>=your_bot_token_here`

**4. Running the Bot**  
After setting up everything, you can run the bot with the following command:
- Activate your virtual environment (if not already active): `source venv/bin/activate`
- Run the bot: `python <bot-file>.py`

## Setting Up Each Bot as a Systemd Service
You can run each bot as a background service using systemd. Follow these steps to create and configure a systemd service for each bot.

**1. Create a systemd Service File**
For each bot, create a service file under `/etc/systemd/system/`. Replace `<bot-name>` with the appropriate bot name (e.g., `zeze`, `chewie`, `chomper`, or `freyja`).

```bash
sudo nano /etc/systemd/system/<bot-name>.service
```

**2. Add the Following Configuration to the Service File**
```bash
[Unit]
Description=Discord Bot - <Bot-Name>
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/your/bot
ExecStart=/path/to/your/venv/bin/python /path/to/your/bot/<bot-file>.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

### Bot-Specific Setup Notes:

- **ZeZe**: Requires a channel ID for announcements. Update the `ANNOUNCEMENT_CHANNEL_ID` in the script.
- **Chewie**: Requires proper role permissions for managing roles.
- **Chomper and Freyja**: Require OpenAI API keys in the environment variables for interacting with the OpenAI API.

## Permissions

All commands across the bots require administrator permissions to ensure only trusted users can execute critical actions.
