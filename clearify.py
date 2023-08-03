#!/usr/bin/env python3
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv
import praw

QUESTIONS = ["what is", "who is", "what are"]
REPLY_TEMPLATE = "[Let me google that for you](https://lmgtfy.com/?q={})"

load_dotenv()


def main():
    reddit = praw.Reddit(
        client_id=os.getenv('APP_KEY'),
        client_secret=os.getenv('APP_SECRET'),
        # password="PASSWORD",
        user_agent="Clearify"
        # username="USERNAME",
    )

    subreddit = reddit.subreddit("ClearifyBot")
    for comment in subreddit.stream.comments():
        print(comment.body)


# def process_submission(submission):
#     # Ignore titles with more than 10 words as they probably are not simple questions.
#     if len(submission.title.split()) > 10:
#         return

#     normalized_title = submission.title.lower()
#     for question_phrase in QUESTIONS:
#         if question_phrase in normalized_title:
#             url_title = quote_plus(submission.title)
#             reply_text = REPLY_TEMPLATE.format(url_title)
#             print(f"Replying to: {submission.title}")
#             submission.reply(reply_text)
#             # A reply has been made so do not attempt to match other phrases.
#             break


if __name__ == "__main__":
    main()
