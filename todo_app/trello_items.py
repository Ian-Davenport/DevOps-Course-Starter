import requests
import os

board = os.getenv('IAN_BOARD')
key = os.getenv('IAN_KEY')
token = os.getenv('IAN_TOKEN')


# response = requests.get(f'https://.api.trello.com/1/boards/{board}/?key={key}&token={token}')
# print(response.json()[0]['cards'][1]['name'])


print(board)
print(key)
print(token)
