
import requests
import json

token = input("Enter your Github access token: ")
org = input("Enter your Orgnization Name: ")
username = input("Enter member user name to remove: ")

url = "https://api.github.com/{}"

path = f"orgs/{org}/members/{username}"

headers = {'Authorization': 'token ' + token}

data ={
    "org" : org,
    "username" : username
}

login = requests.delete(url.format(path) , headers=headers , json = data )
#print(login.json())


print(login.status_code)
