#!/usr/bin/env python3
import os

import praw
from dotenv import load_dotenv

from functions import clearify, get_modifier
import templates


load_dotenv()


def main():
    # Load environment variables
    reddit = praw.Reddit(
        client_id=os.getenv('APP_KEY'),
        client_secret=os.getenv('APP_SECRET'),
        user_agent="Clearify Helper Script to clear up and clairify by u/seth_b5t",
        refresh_token=os.getenv('REFRESH_TOKEN'),
    )

    subreddit = reddit.subreddit("all")
    for comment in subreddit.stream.comments():
        # if comment contains !clearify and is not saved yet
        if "!clearify" in comment.body.lower() and not comment.saved:
            print(comment.body)
            # get the level of clearification
            level = get_modifier(comment.body)
            print(
                f"Comming right up! Let me Clerify for you being a {level}:\n{comment.parent().body}")

            # make the clearification
            clear = clearify(comment.parent().body, level)
            # get the clearification message
            message = clear['choices'][0]['message']['content']
            # reply to the comment with the message
            comment.reply(message + templates.FOOTER_TEMPLATE)
            # save the comment so that we don't reply to it again
            comment.save()
            print("DONE!")


if __name__ == "__main__":
    main()
