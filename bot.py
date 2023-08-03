#!/usr/bin/env python

import praw
from prawoauth2 import PrawOAuth2Mini

from tokens import app_key, app_secret, access_token, refresh_token
from settings import scopes, user_agent
from dotenv import load_dotenv
load_dotenv()

reddit_client = praw.Reddit(user_agent=user_agent)
oauth_helper = PrawOAuth2Mini(reddit_client, app_key=app_key,
                              app_secret=app_secret, access_token=access_token,
                              scopes=scopes, refresh_token=refresh_token)


def explain_loop():
    oauth_helper.refresh()
    for comment in reddit_client.get_comments('all'):
        if '!ExplainThis' in comment.body.lower():
            print('Comming right up!')
            comment.reply('Sure thing!')


while True:
    try:
        explain_loop()
    except praw.errors.OAuthInvalidToken:
        # token expired, refresh 'em!
        oauth_helper.refresh()
