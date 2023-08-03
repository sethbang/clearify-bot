
# Clearify Bot

This is a Reddit bot that clarifies parent comments when a user replies with "!clearify". 

## What it does

- Monitors the Reddit stream for new comments containing "!clearify"
- Checks if the comment has already been processed to avoid duplicate replies
- Extracts the parent comment that needs clarifying
- Calls the OpenAI API to generate a clarified version of the parent comment
- Replies to the original comment with the clarified text
- Saves the comment to mark it as processed

## Usage

To use the bot:

1. Reply to any comment with "!clearify"
2. The bot will reply clarifying the parent comment

You can also add a modifier in the format `@ [modifier] @` to customize the clarification:

```
!clearify @ 5 year old @
```

This will generate an explanation suitable for a 5 year old.

Some examples of modifiers:

- 5 year old - Explain Like I'm 5 
- Stoner - Explain for a stereotypical stoner
- Grandma - Explain simply for your grandma
- Programmer - Explain using technical jargon

## Setup

To run the bot yourself:

1. Clone this repo
2. Copy .env.example to .env and add your API keys
3. Install requirements with `pip install -r requirements.txt` 
4. Run `python clearify.py`

You will need:

- Reddit API credentials
- OpenAI API key

## Customization

You can customize the bot by editing:

- `FOOTER_TEMPLATE` - The footer appended to all replies 
- `clearify()` - The OpenAI prompt and parameters
- `main()` - The subreddit(s) streamed and logic

## Limitations

- Only clarifies parent comments, not top level posts
- Only processes new comments, does not backfill
- Basic clarification, no other conversational abilities

Let me know if you need any clarification or have additional questions!