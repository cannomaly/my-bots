<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZeZe</title>
</head>
<body>
    <h1>ZeZe is my personal discord bot. It's also the name of my Middle son's french builldog</h1>
    <p>
        A powerful and feature-rich Discord bot tailored for server administrators to manage and send announcements in a streamlined and organized way. It includes features for scheduling announcements, urgent notifications, and logging past messages.
    </p>

    <h2>Features</h2>
    <ul>
        <li><strong>Scheduled Announcements:</strong>
            <ul>
                <li>Use the <code>!schedule_announce HH:MM message</code> command to schedule an announcement for a specific time (24-hour format).</li>
                <li>Example: <code>!schedule_announce 14:30 Server maintenance will start soon!</code> will schedule a message at 14:30.</li>
            </ul>
        </li>
        <li><strong>Immediate Announcements:</strong>
            <ul>
                <li>Send an instant announcement to the designated announcement channel using the <code>!announce message</code> command.</li>
                <li>Example: <code>!announce Server update is live!</code> will post the announcement immediately.</li>
            </ul>
        </li>
        <li><strong>Urgent Announcements:</strong>
            <ul>
                <li>Use the <code>!urgent_announce message</code> command to send high-priority, urgent announcements with special formatting.</li>
                <li>Example: <code>!urgent_announce Critical server downtime!</code> will send an alert with an urgent tag.</li>
            </ul>
        </li>
        <li><strong>Announcement Logs:</strong>
            <ul>
                <li>Keep track of all past announcements using the <code>!view_log</code> command, showing previous announcements along with their timestamps and authors.</li>
            </ul>
        </li>
        <li><strong>View Scheduled Announcements:</strong>
            <ul>
                <li>Admins can use the <code>!view_schedule</code> command to view all upcoming scheduled announcements.</li>
            </ul>
        </li>
        <li><strong>Channel-Specific Announcements:</strong>
            <ul>
                <li>All announcements are sent to a predefined announcement channel (set by <code>ANNOUNCEMENT_CHANNEL_ID</code> in the code).</li>
            </ul>
        </li>
        <li><strong>Backup and Restore:</strong>
            <ul>
                <li>The bot keeps a log of all announcements that can act as a simple backup of past messages.</li>
            </ul>
        </li>
    </ul>

    <h2>Setup Instructions</h2>
    
    <h3>1. Clone the Repository</h3>
    <p>
        Download the bot's repository to your local machine using the following command:<br>
        <code>git clone https://github.com/cannomaly/announcement-bot.git</code><br>
        <code>cd announcement-bot</code>
    </p>

    <h3>2. Install Dependencies</h3>
    <p>
        Make sure Python 3.8+ is installed. Set up a Python virtual environment and install the required dependencies by running the following commands:<br>
        Create a virtual environment: <code>python3 -m venv venv</code><br>
        Activate the virtual environment: <code>source venv/bin/activate</code> (for Linux/macOS) or <code>.\venv\Scripts\activate</code> (for Windows)<br>
        Install dependencies: <code>pip install -r requirements.txt</code>
    </p>

    <h3>3. Set Up Environment Variables</h3>
    <p>
        Create a <code>.env</code> file in the root directory of the project. Add your bot token to the file like so:<br>
        <code>DISCORD_TOKEN_ZEZE=your_bot_token_here</code>
    </p>

    <h3>4. Set the Announcement Channel</h3>
    <p>
        In the bot's code, locate the <code>ANNOUNCEMENT_CHANNEL_ID</code> variable. Replace the value with your Discord server's announcement channel ID:<br>
        <code>ANNOUNCEMENT_CHANNEL_ID = 1288274033154199594</code> (Replace this with your channel's ID)
    </p>

    <h3>5. Running the Bot</h3>
    <p>
        After setting up everything, you can run the bot with the following commands:<br>
        Activate your virtual environment (if not already active): <code>source venv/bin/activate</code><br>
        Run the bot: <code>python bot.py</code>
    </p>

    <h2>Bot Commands</h2>
    
    <h3>1. <code>!announce message</code></h3>
    <p><strong>Description:</strong> Send an immediate announcement to the designated channel.</p>
    <p><strong>Example:</strong> <code>!announce Server will be down for maintenance.</code></p>

    <h3>2. <code>!schedule_announce HH:MM message</code></h3>
    <p><strong>Description:</strong> Schedule an announcement to be sent at a specific time (24-hour format).</p>
    <p><strong>Example:</strong> <code>!schedule_announce 09:00 Daily server check.</code></p>

    <h3>3. <code>!urgent_announce message</code></h3>
    <p><strong>Description:</strong> Send an urgent announcement to the channel, marked with priority formatting.</p>
    <p><strong>Example:</strong> <code>!urgent_announce Security alert! Server breach detected.</code></p>

    <h3>4. <code>!view_log</code></h3>
    <p><strong>Description:</strong> View the log of all past announcements, including timestamps and authors.</p>

    <h3>5. <code>!view_schedule</code></h3>
    <p><strong>Description:</strong> View all upcoming scheduled announcements.</p>

    <h2>Permissions</h2>
    <p>All commands require the administrator permission to execute, ensuring only trusted users can make announcements.</p>
</body>
</html>
