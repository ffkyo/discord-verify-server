import os
token = os.environ.get("BOT_TOKEN", "platzhalter")

# Deine Server-IDs
guildid = "1490783176992227328"
roleid = "1490783637896167600"

# Discord Application
CLIENT_ID = "1504241186968305804"
CLIENT_SECRET = "YHzP1yzYTo5uMvCqgSJ1t2FkIg4408qZ"

# Wichtig: Erstmal Platzhalter, nach Render-Setup ersetzen!
BASE_URL = "https://discord-verify-server.onrender.com"

# Deine Render-IP
WEB_IP = "0.0.0.0"
WEB_PORT = 10000  # Render nutzt Port 10000 oder Umgebungsvariable

REDIRECT_URI = BASE_URL + '/callback'
oauth2_url = f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify%20guilds%20guilds.join&state={guildid}"
API_ENDPOINT = "https://discord.com/api/v9"

BOLD = '\033[1m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
