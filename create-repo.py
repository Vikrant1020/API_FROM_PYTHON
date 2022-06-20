
import requests
import json

url = "https://api.github.com/{}"

path = "user/repos"

repo_name = input("Enter your new repo name: ")
token = input("Enter your personal access token: ")


headers = {'Authorization': 'token ' + token}

data ={
    "name" : repo_name
}

login = requests.post(url.format(path), headers=headers , json=data)
print(login.status_code)
# print(login.json())