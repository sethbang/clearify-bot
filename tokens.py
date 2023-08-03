import os
from dotenv import load_dotenv

load_dotenv()

app_key = os.getenv('APP_KEY')
app_secret = os.getenv('APP_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
refresh_token = os.getenv('REFRESH_TOKEN')
