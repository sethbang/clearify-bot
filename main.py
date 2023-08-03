import praw
from prawoauth2 import PrawOAuth2Server, PrawOAuth2Mini
from dotenv import load_dotenv
import os

load_dotenv()
app_key = os.getenv('APP_KEY')
app_secret = os.getenv('APP_SECRET')

user_agent = 'explainthisbot'
reddit_client = praw.Reddit(user_agent=user_agent)
scopes = ['identity', 'read', 'submit']

oauthserver = PrawOAuth2Server(reddit_client, app_key, app_secret,
                               state=user_agent, scopes=scopes)

oauthserver.start()
tokens = oauthserver.get_access_codes()

oauth_helper = PrawOAuth2Mini(reddit_client, app_key=app_key,
                              app_secret=app_secret,
                              access_token=access_token,
                              refresh_token=refresh_token, scopes=scopes)
