import datetime
import requests
import json

UserName = input("Enter your Github user name : ")
url = "https://api.github.com/{}"

type_of_repo = input("For all repo type 'a' for Public only type 'p' :" )
print(type_of_repo)
if (type_of_repo.lower() == 'p'):
        
    path = f"users/{UserName}/repos"

    response = requests.get(url.format(path))

    data = response.json()  # Data in List data type.
    len = len(data)    

    print("Yours Public repos are as following :")
    for i in range(len):
        repo = data[i]     # data have dict datatype. 
        print(i+1, repo["name"] ) 
        a = repo["name"]
        b = f"{datetime.datetime.now()} {a}, \n"
        with open("Publiclogs.json", "a") as outfile:
            outfile.write(b )

elif (type_of_repo.lower() == 'a'):

    token = input("Enter your git hub access token : ")
    path = f"user/repos"

    headers = {'Authorization': 'token ' + token}

    response = requests.get(url.format(path) , headers=headers)

    data = response.json()  # Data in List data type.
    len = len(data)    

    print("Yours Public repos are as following :")
    for i in range(len):
        repo = data[i]     # data have dict datatype. 
        print(i+1, repo["name"] ,"...............Privte :" , repo["private"])        # print total no. and name of repos in your Github account.
        a = repo["name"]
        c = repo["private"]
        b = f"{datetime.datetime.now()} {a}------------ private:-- {c}, \n"
        with open("Privatelogs.json", "a") as outfile:
            outfile.write(b )
else:
    print("PK ho kya")
    


