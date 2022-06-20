
import requests
import json

token = input("Enter your Github access token: ")
org = input("Enter your Orgnization Name: ")
email = input("Enter Email to add in your Orgnization: ")

url = "https://api.github.com/{}"

path = f"orgs/{org}/invitations"

headers = {'Authorization': 'token ' + token}

data ={
    "org" : org,
    "email" : email
}

login = requests.post(url.format(path) , headers=headers , json = data )
#print(login.json())


print(login.status_code)