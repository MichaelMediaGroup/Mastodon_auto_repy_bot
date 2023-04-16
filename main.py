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
followering = mastodon.account_following(110090602223960345)
with open("jokes.txt", "r") as f:
    jokes = f.readlines()

jokes = []

while True:
    #if a follower creats a new post
    for follower in followering:
        follower_posts = mastodon.account_statuses(follower.id)
        for post in follower_posts:
            if post.favourited == False:
                #like the post
                mastodon.status_favourite(post.id)
                #reply to the post
                mastodon.status_post("@" + post.account.acct + " " + random.choice(["Hello", "Hi", "Hey", "Greetings"]), in_reply_to_id=post.id)