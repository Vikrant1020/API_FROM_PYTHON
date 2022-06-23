import os
import slack


token_user =  input("Enter your User token: ")
token_bot =  input("Enter your Bot token : ")

client = slack.WebClient(token=token_user )
client.chat_postMessage(channel = '#python_api' , text = 'Mesage from User')

bot = slack.WebClient(token = token_bot)
bot.chat_postMessage(channel = "#python_api", text = "Mesasge from BOt")