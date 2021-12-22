import requests
import dotenv
import os
dotenv.load_dotenv("../.env")

IAN_KEY = os.getenv("IAN_KEY")
IAN_TOKEN = os.getenv("IAN_TOKEN")
IAN_BOARD = os.getenv("IAN_BOARD")


IN_PROGRESS = "619fcb801249d837919f8966"
CARD = "61a66358d56e1381cb97f284"
url = f"https://api.trello.com/1/cards/{CARD}?idList={IN_PROGRESS}&key={IAN_KEY}&token={IAN_TOKEN}"

response = requests.put(url)
print(response.text)

