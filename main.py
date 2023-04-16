from mastodon import Mastodon
import time
from dotenv import load_dotenv
import os
import random

load_dotenv()

mastodon = Mastodon(
    client_id=os.getenv("Client_key"),
    client_secret=os.getenv("Client_secret"),
    access_token=os.getenv("access_token"),
    api_base_url="https://mastodon.social"
)

following = mastodon.account_following(110209472762362718)

followering_posts = []
for i in following:
    for posts in mastodon.account_statuses(i):
        followering_posts.append(posts.id)

print(followering_posts)

with open("jokes.txt", "r") as f:
    jokes = f.readlines()

while True:
    for i in following:
        for posts in mastodon.account_statuses(i):
            if posts.id not in followering_posts:
                followering_posts.append(posts.id)
                joke_used = random.choice(jokes)
                mastodon.status_post(joke_used,in_reply_to_id=posts.id)

    time.sleep(120)