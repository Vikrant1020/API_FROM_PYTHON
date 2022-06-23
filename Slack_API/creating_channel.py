import os
from slack import WebClient

token_user =  input("Enter your User token: ")

client = WebClient(token=token_user)
channel_name = input("Enter your channel name")
response = client.conversations_create(
  name=channel_name,
  is_private=False,
  is_archive=False
)
print(response)