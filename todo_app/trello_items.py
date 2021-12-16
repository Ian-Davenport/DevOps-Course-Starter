import requests
import os

board = os.getenv('IAN_BOARD')
key = os.getenv('IAN_KEY')
token = os.getenv('IAN_TOKEN')
todo = os.getenv('TO_DO_ID')
inprog = os.getenv('IN_PROGRESS_ID')
done = os.getenv('DONE_ID')


# response = requests.get(f'https://.api.trello.com/1/boards/{board}/?key={key}&token={token}')
# print(response.json()[0]['cards'][1]['name'])
# print(board)
# print(key)
# print(token)


def fetch_todo():
    call = f"https://api.trello.com/1/boards/{board}/lists?key={key}&token={token}&cards=open"
    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        "GET",
        url=call,
        headers=headers
    )
    result = response.json()
    for item in result:
        if item["name"] == "To-Do":
            return item["cards"]


def fetch_in_progress():
    call = f"https://api.trello.com/1/boards/{board}/lists?key={key}&token={token}&cards=open"
    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        "GET",
        url=call,
        headers=headers
    )
    result = response.json()
    for item in result:
        if item["name"] == "In Progress":
            return item["cards"]


def fetch_done():
    call = f"https://api.trello.com/1/boards/{board}/lists?key={key}&token={token}&cards=open"
    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        "GET",
        url=call,
        headers=headers
    )
    result = response.json()
    for item in result:
        if item["name"] == "DONE!":
            return item["cards"]


def add_task():
    call = f"https://api.trello.com/1/lists/{todo}/cards?name={title}&key={key}&token={token}"
    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        "POST",
        url=call,
        headers=headers
    )

# NEEDS AMENDING


def move_task():
    call = f"https://api.trello.com/1/lists/{todo}/cards?name={title}&key={key}&token={token}"
    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        "PUT",
        url=call,
        headers=headers
    )


def delete_task(id):
    call = f"https://api.trello.com/1/cards/{id}?key={key}&token={token}"
    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        "DELETE",
        url=call,
        headers=headers
    )
