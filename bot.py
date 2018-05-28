import json
import os
import time

import praw
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client_id=os.environ['REDDIT_CLIENT_ID']
client_secret=os.environ['REDDIT_CLIENT_SECRET']
password=os.environ['REDDIT_PASSWORD']
username=os.environ['REDDIT_USERNAME']
user_agent='user-agent for /u/stoicbot'

FOOTER_STRING = '''




This bot was created by [xtreak](https://www.reddit.com/r/xtreak). Please contact the author for any bugs or raise issues in GitHub. The source code is at [GitHub](https://www.github.com/tirkarthi/stoicbot). Feedback is welcome.
'''

def main():
    with open('text/content.json') as data_file:
        data = json.load(data_file)

    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         password=password,
                         username=username,
                         user_agent=user_agent)

    while True:
        print("Waiting for a reply")
        for comment in reddit.inbox.unread(limit=25):
            print("Got mention from {0} with body {1}".format(comment.author, comment.body))
            quote = None
            body = comment.body

            if body:
                mention, quote = body.split(' ')
                quote = quote.strip()
                quote = data.get(quote)
                if quote:
                    quote = quote + FOOTER_STRING
                    comment.reply(quote)
                    comment.mark_read()
                else:
                    comment.mark_read()
                    print("No quotes for this. Please specify in the format 'chapter_number.verse_number'")
            else:
                comment.mark_read()
                print("No quotes for this. Please specify in the format 'chapter_number.verse_number'")

        # Don't hit reddit server for every second
        time.sleep(10)

if __name__ == "__main__":
    main()
