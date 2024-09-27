# ZeZe - Personal Announcement Discord Bot

*ZeZe is my personal Discord bot. It's also the name of my middle son's French bulldog.*

A powerful and feature-rich Discord bot tailored for server administrators to manage and send announcements in a streamlined and organized way. It includes features for scheduling announcements, urgent notifications, and logging past messages.

## Features

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

- **Channel-Specific Announcements**:  
  All announcements are sent to a predefined announcement channel (set by `ANNOUNCEMENT_CHANNEL_ID` in the code).

- **Backup and Restore**:  
  The bot keeps a log of all announcements that can act as a simple backup of past messages.

## Setup Instructions

### 1. Clone the Repository
Download the bot's repository to your local machine using the following command:
```bash
git clone https://github.com/cannomaly/announcement-bot.git
cd announcement-bot
```

### 2. Install Dependencies
Make sure Python 3.8+ is installed. Set up a Python virtual environment and install the required dependencies by running the following commands:
- Create a virtual environment: `python3 -m venv venv`
- Activate the virtual environment: `source venv/bin/activate` (for Linux/macOS) or `.\venv\Scripts\activate` (for Windows)
- Install dependencies: `pip install -r requirements.txt`

### 3. Set Up Environment Variables
Create a `.env` file in the root directory of the project. Add your bot token to the file like so:
```bash
DISCORD_TOKEN_ZEZE=your_bot_token_here
```

### 4. Set the Announcement Channel
- In the bot's code, locate the `ANNOUNCEMENT_CHANNEL_ID` variable.
- Replace the value with your Discord server's announcement channel ID:
```bash
ANNOUNCEMENT_CHANNEL_ID = 1288274033154199594 # Replace this with your channel's ID
```

### 5. Running the Bot

After setting up everything, you can run the bot with the following command:
- Activate your virtual environment (if not already active): `source venv/bin/activate`
- Run the bot: `python bot.py`

## Bot Commands

### 1. !announce message
- **Description**: Send an immediate announcement to the designated channel.
- **Example**: `!announce Server will be down for maintenance.`

### 2. !schedule_announce HH:MM message
- **Description**: Schedule an announcement to be sent at a specific time (24-hour format).
- **Example**: `!schedule_announce 09:00 Daily server check.`

### 3. !urgent_announce message
- **Description**: Send an urgent announcement to the channel, marked with priority formatting.
- **Example**: `!urgent_announce Security alert! Server breach detected.`

### 4. !view_log
- **Description**: View the log of all past announcements, including timestamps and authors.

### 5. !view_schedule
- **Description**: View all upcoming scheduled announcements.

### 6. !help
- **Description**: Display a list of all available commands for administrators.

## Permissions
All commands require the administrator permission to execute, ensuring only trusted users can make announcements.
