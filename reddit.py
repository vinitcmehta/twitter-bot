from pprint import pprint
import requests
import json

url = 'https://www.reddit.com/r/todayilearned/top/.json?t=day'
headers = requests.utils.default_headers()
default_agent = headers['User-Agent']
print(default_agent)
headers.update(
    {
        'User-Agent': 'vinit',
    }
)

response = requests.get(url, headers=headers)
print(response.text)
print(response.json())
data = response.json()
print(data.keys())
print(data['data']['children'][0]['data']['title'])
reddit_title = data['data']['children'][0]['data']['title']
reddit_fact = reddit_title[4:]
print(reddit_fact)
#MUST BE 280 or less, choose next if not chosen?, may have to store already printed facts
print(len(reddit_fact))

for child in data['data']['children']:
    print (child['data']['id'])
    print(child['data']['title'])
