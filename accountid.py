from mastodon import Mastodon
import os
from dotenv import load_dotenv

load_dotenv()

mastodon = Mastodon(
    client_id=os.getenv("Client_key"),
    client_secret=os.getenv("Client_secret"),
    access_token=os.getenv("access_token"),
    api_base_url="https://mastodon.social"
)

#get my account id
my_account = mastodon.account_verify_credentials()
print(my_account.id)

