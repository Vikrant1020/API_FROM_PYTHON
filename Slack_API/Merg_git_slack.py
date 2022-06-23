import requests
import json
import os

def slack():

    ############### SLACK API ###############

    Slack_URL = "https://hooks.slack.com/services/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"


    file = open ("repo.txt" , "r")

    results = f"Selected Repos are for user {UserName}\n{file.read()}"
    response =  requests.post(Slack_URL , json={'text': str(results), "color" : "#f2c744"})

    # print(response.text)
    # print(response.status_code)
    
    file.close()

    os.remove("repo.txt")
    

############### GIT API ##################

UserName = input("Enter your Github user name : ")
GIT_URL = "https://api.github.com/{}"

type_of_repo = input("For all repo type 'a' for Public only type 'p' :" )
if (type_of_repo.lower() == 'p'):
    
    path = f"users/{UserName}/repos"

    response = requests.get(GIT_URL.format(path))

    data = response.json()  # Data in List data type.
    len = len(data)    

    print("\n################ Output dispacted on Slack ################")
    for i in range(len):
        repo = data[i]     # data have dict datatype. 
        a = repo["name"]
        c = repo["private"]
        b = f"{a}------------ private:-- {c}, \n"
        with open("repo.txt", "a") as outfile:
            outfile.write(b)
    slack()

elif (type_of_repo.lower() == 'a'):

    token = input("Enter your git hub access token : ")
    path = f"user/repos"

    headers = {'Authorization': 'token ' + token}

    response = requests.get(GIT_URL.format(path) , headers=headers)

    data = response.json()  # Data in List data type.
    len = len(data)    

    print("\n################ Output dispacted on Slack ################ ")
    for i in range(len):
        repo = data[i]     # data have dict datatype. 
        a = repo["name"]
        c = repo["private"]
        b = f"{a}------------ private:-- {c}, \n"
        with open("repo.txt", "a") as outfile:
            outfile.write(b)
    slack()

else:
    print("\n\nP ya A likhne ko bola h na \nKuch aur kaiko Likh ra h \nPK ho ka")
    
