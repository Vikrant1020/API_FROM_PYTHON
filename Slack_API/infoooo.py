import slack
import os
from slack import WebClient

token_user =  input("Enter your User token: ")
client = WebClient(token = token_user)

channel = input ("Enter your channel ID : ")
response = client.conversations_info(channel = channel)
print(response)