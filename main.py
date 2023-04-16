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

#get account id
followering = mastodon.account_following(110209472762362718)
with open("jokes.txt", "r") as f:
    jokes = f.readlines()


followering_posts = []

for i in followering:
    for post in mastodon.account_statuses(i):
        followering_posts.append(post.id)

print(followering_posts)


while True:
    #check if there are new posts
    for i in followering:
        for post in mastodon.account_statuses(i):
            if post.id not in followering_posts:
                followering_posts.append(post.id)
                print("New post")
                selected_joke = random.choice(jokes)
                mastodon.status_post(selected_joke, in_reply_to_id=post.id)

    time.sleep(60)

    