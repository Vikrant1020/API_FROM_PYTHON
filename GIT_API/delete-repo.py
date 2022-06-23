
import requests
import json

username = input("Enter your Github user name: ")
reponame = input("Enter repo name you want to delete: ")
token = input("Enter your personal access token: ")

url = "https://api.github.com/{}"

path = f"repos/{username}/{reponame}"

headers = {'Authorization': 'token ' + token}

# data ={
#     "name" : "TestingAPI"
# }

login = requests.delete(url.format(path), headers=headers)

# print(login.json())

print(login.status_code)