import requests
import os
from todo_app.todo_item import TodoItem

board = os.getenv('IAN_BOARD')
key = os.getenv('IAN_KEY')
token = os.getenv('IAN_TOKEN')
todo = os.getenv('TO_DO')
inprog = os.getenv('IN_PROGRESS')
done = os.getenv('DONE')




def fetch_list():
    call = f"https://api.trello.com/1/boards/{os.getenv('IAN_BOARD')}/lists"
    query_string_dictionary = {
        "key": os.getenv('IAN_KEY'),
        "token": os.getenv('IAN_TOKEN'),
        "cards": "open"
    }
    
    response = requests.get(
        url=call,
        params=query_string_dictionary
    )

    result = response.json()

    tasks = []
    for list in result:
        for card in list['cards']:
            task = TodoItem.from_trello_card(card, list["name"])
            tasks.append(task)
    return tasks


def new_todo(title):
    call = f"https://api.trello.com/1/lists/{todo}/cards?name={title}&key={key}&token={token}"

    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        "POST",
        url=call,
        headers=headers
    )


def move_to_done(id):
    call = f"https://api.trello.com/1/cards/{id}?idList={done}&key={key}&token={token}"

    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        "PUT",
        url=call,
        headers=headers
    )


def move_to_inprog(id):
    call = f"https://api.trello.com/1/cards/{id}?idList={inprog}&key={key}&token={token}"

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
