
from tokenize import single_quoted
from slack import WebClient
from flask import Flask
from slackeventsapi import SlackEventAdapter

token =  input("Enter your Bot token or User token: ")
sing_token = input("enter your sing token: ")

global response
response = input("Enter message:  ")

client = WebClient(token= token)




app = Flask(__name__)
slack_adpter = SlackEventAdapter(sing_token , '/slack/events', app)

Bot_id = client.api_call("auth.test")['user_id']

@slack_adpter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    text = event.get('text')
    user_id = event.get('user')
    
    if Bot_id != user_id:
        client.chat_postMessage(channel= channel_id , text = response)

if (__name__ == "__main__" ):
    app.run(debug=True)