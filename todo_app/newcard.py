# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import json
import requests
import dotenv
from dotenv import load_dotenv
import os
dotenv.load_dotenv("../.env")

IAN_KEY = os.getenv("IAN_KEY")
IAN_TOKEN = os.getenv("IAN_TOKEN")
IAN_BOARD = os.getenv("IAN_BOARD")
LIST_ID = os.getenv("LIST_ID")
name = "DOES THIS WORK"

url = "https://api.trello.com/1/cards?idList={LIST_ID}&key={IAN_KEY}&token={IAN_TOKEN}&name={name}"


headers = {
    "Accept": "application/json"
}

query = {
    # 'idList': '5abbe4b7ddc1b351ef961414'  # UNSURE WHERE THIS LIST IS....
    'idList': '619fcb801249d837919f8965'   # THIS IS THE TO-DO LIST ID
}

response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
)

print(json.dumps(json.loads(response.text),
      sort_keys=True, indent=4, separators=(",", ": ")))
