from prettytable import PrettyTable
import requests

# table = PrettyTable()
# table.field_names = ["Key", "Value"]

response = requests.get("https://api.github.com/users/vikrant1020/repos")  

print(response.status_code)
print(type(response))
# data = response.json()

# for key, value in data.items():
#     table.add_row([key, value])

# print(table)

