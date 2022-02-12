import requests

url = 'https://api.stackexchange.com/2.3/questions'
params = {
    'fromdate': '2022-02-10',
    'todate': '2022-02-12',
    'order': 'desc',
    'sort': 'activity',
    'tagged': 'python',
    'site': 'stackoverflow'
}

response = requests.get(url, params=params)

for item in response.json()['items']:
    print(item['question_id'], ':', item['title'])

