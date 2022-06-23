import requests
import json
import base64

# owner = input("Enter Owner name: ")
# repo = input("input repo name: ")
path = input("enter path to add: ")
owner = "vikrant1020"
repo = "Django"
token = input("Enter your personal access token: ")

# text = "Made through API".encode("utf-8")
# content = base64.b64encode(text)
# print(content)


url = "https://api.github.com/{}"
root_url = f"repos/{owner}/{repo}/contents/{path}"



headers = {'Authorization': 'token ' + token}
data ={
    "owner" : owner,
    "repo" : repo,
    "path" : path,
    "message": "commit through API",
    "content": 'Hello welcome', 
    "committer": {
    "name" : 'vikrant1020',
    "email" : 'ankur.thankur1020@gamil.com'
  },
    "brnch": "master"
}

login = requests.put(url.format(root_url), headers=headers , json=data)
print(login.status_code)
print(login.json())