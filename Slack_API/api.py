
import requests

results = input ("Enter your message:\n")

response =  requests.post("https://hooks.slack.com/services/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" , json={'text': str(results)})

new_result = f"python API is getting message {results}"
response1 = requests.post("https://hooks.slack.com/services/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", json={'text': str(new_result)})

# print(response.text)
# print(response.status_code)
# print(response1.text)
# print(response1.status_code)
