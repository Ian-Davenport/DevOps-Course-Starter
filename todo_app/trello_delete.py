import requests
import dotenv
import os

dotenv.load_dotenv("../.env")

IAN_KEY=os.getenv("IAN_KEY")
IAN_TOKEN=os.getenv("IAN_TOKEN")
IAN_BOARD=os.getenv("IAN_BOARD")
CARD = "619ff64a11bac354af28058d"


url = f"https://api.trello.com/1/cards/{CARD}?key={IAN_KEY}&token={IAN_TOKEN}"



response = requests.delete(url)

print(response.text)
