import requests
import json

UserName = input("Enter your Github user name : ")
url = "https://api.github.com/{}"

token = input("Enter your git hub access token : ")
path = f"user/repos"

headers = {'Authorization': 'token ' + token}

response = requests.get(url.format(path) , headers=headers)

data = response.json()  # Data in List data type.
len = len(data)    

print("Yours Public repos are as following :")
for i in range(len):
    repo = data[i]     # data have dict datatype. 
    print(i+1, repo["name"])        # print total no. and name of repos in your Github account.



