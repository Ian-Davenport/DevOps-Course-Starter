import requests
import dotenv
import os

dotenv.load_dotenv("../.env")

IAN_KEY = os.getenv("IAN_KEY")
IAN_TOKEN = os.getenv("IAN_TOKEN")
IAN_BOARD = os.getenv("IAN_BOARD")


url = f"https://api.trello.com/1/boards/{IAN_BOARD}/lists?key={IAN_KEY}&token={IAN_TOKEN}&cards=open"


# url = F"https://api.trello.com/1/boards/{IAN_BOARD}/cards?key={IAN_KEY}&token={IAN_TOKEN}&cards=open""


response = requests.get(url)

print(response.text)

# THIS WORKS IN GETTING ALL THE BOARD

#   json.loads(response.text)   returns json file
# json_response = json.loads(response.text)
# type(json_response)
# <class 'list'>
# response.json()

# #####  BOARD LISTS  #######
# To Do:  619fcb801249d837919f8965
# In Progress:  619fcb801249d837919f8966
# Needs Work:  619fcb801249d837919f8967
# DONE!:  619fcb801249d837919f8968
