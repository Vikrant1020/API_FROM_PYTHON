import requests as bj

url = "https://hooks.slack.com/services/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"

data = {
	"attachments": [
		{
			"color": "#f2c744",
			"blocks": [
				{
					"type": "header",
					"text": {
						"type": "plain_text",
						"text": "Testing",
						"emoji": True
					}
				},
				{
					"type": "section",
					"fields": [
						{
							"type": "mrkdwn",
							"text": "*Type:*\nTesting API"
						},
						{
							"type": "mrkdwn",
							"text": "*Created by:*\n<seasia.com|Fred Enriquez>"
						}
					]
				},
				{
					"type": "section",
					"fields": [
						{
							"type": "mrkdwn",
							"text": "*When:*\n 22 AUG 2022"
						}
					]
				},
				{
					"type": "section",
					"text": {
						"type": "plain_text",
						"text": "Ready to Launch",
						"emoji": True
					}
				}
			]
		}
	]
}

output = bj.post(url , json = data)

print(output.text)
print(output.status_code)