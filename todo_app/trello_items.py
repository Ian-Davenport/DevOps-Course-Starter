import requests
import os
import json


board = os.getenv('IAN_BOARD')
key = os.getenv('IAN_KEY')
token = os.getenv('IAN_TOKEN')
todo = os.getenv('To-Do')
inprog = os.getenv('In_Progress')
done = os.getenv('DONE!')
list_id = os.getenv('LIST_ID')


class Item:
    def __init__(self, id, name, status='To Do'):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card, list_name):
        return cls(card['id'], card['name'], list_name)

##############################################################################################


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
    # for item in result:
    #     if item["name"] == "To-Do":
    #         return item["cards"]

    tasks = []
    for item in result:
        if item['name'] == 'To-Do':
            for card in item['cards']:
                task = Item.from_trello_card(card, "To-Do")
                tasks.append(task)
    return tasks


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
    # for item in result:
    #     if item["name"] == "In Progress":
    #         return item["cards"]

    tasks = []
    for item in result:
        if item['name'] == 'In Progress':
            for card in item['cards']:
                task = Item.from_trello_card(card, "In Progress")
                tasks.append(task)
    return tasks


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
    # for item in result:
    #     if item["name"] == "DONE!":
    #         return item["cards"]

    tasks = []
    for item in result:
        if item['name'] == 'DONE!':
            for card in item['cards']:
                task = Item.from_trello_card(card, "DONE!")
                tasks.append(task)
    return tasks

##############################################################################################


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

##############################################################################################


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

##############################################################################################


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

##############################################################################################


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

##############################################################################################
