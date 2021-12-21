import requests
import os

board = os.getenv('IAN_BOARD')
key = os.getenv('IAN_KEY')
token = os.getenv('IAN_TOKEN')
todo = os.getenv('TO_DO_ID')
inprog = os.getenv('IN_PROGRESS_ID')
done = os.getenv('DONE_ID')
list_id = os.getenv('LIST_ID')

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

##############################################################################################


def new_todo(name):
    # new_card_url = f"https://api.trello.com/1/lists/{todo}/cards"
    new_card_url = f"https://api.trello.com/1/cards"

    # headers = {
    #     "Accept": "application/json"
    # }
    # response = requests.request(
    #     "POST",
    #     url=call,
    #     headers=headers
    # )

    new_card_parameters = {
        "key": key,
        "token": token,
        "idList": list_id,
        "name": name
    }

    response = requests.post(new_card_url, parameters=new_card_parameters)

##############################################################################################


def move_todo():
    # call = f"https://api.trello.com/1/lists/{todo}/cards?name={title}&key={key}&token={token}"

    # AMENDED 2ND FEATURE TO LIST_ID >>>
    call = f"https://api.trello.com/1/lists/{todo}/cards?idList={list_id}&key={key}&token={token}"

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

# WORKING FEATURES USING localhost:5000

# DELETE CARD (from 'To-Do' column)
# ADD NEW CARD (in 'To-Do' column)


#  FEATURES TO ADD >>
#  GET NEW 'TO-DO' FORM TO WORK
#  Move from 'To-Do' to 'In Progress"
#  Mark a task as 'Complete'
#  Move from 'In progress' to 'Done'
