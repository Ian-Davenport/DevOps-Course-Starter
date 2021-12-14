import requests
import os

board = os.getenv('IAN_BOARD')
key = os.getenv('IAN_KEY')
token = os.getenv('IAN_TOKEN')


# response = requests.get(f'https://.api.trello.com/1/boards/{board}/?key={key}&token={token}')
# print(response.json()[0]['cards'][1]['name'])


# print(board)
# print(key)
# print(token)


def fetch_all():
    call = f"https://api.trello.com/1/boards/{board}/lists?key={key}&token={token}&cards=open"
    headers = {
        "Accept": "application/json"
    }

    response = requests.request("GET", url=call, headers=headers)

    result = response.json()
    for item in result:
        if item['name'] == 'To-Do':
            return item['cards']
