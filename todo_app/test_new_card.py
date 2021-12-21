# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import json
import requests
import dotenv
import os
dotenv.load_dotenv("../.env")

IAN_KEY = os.getenv("IAN_KEY")
IAN_TOKEN = os.getenv("IAN_TOKEN")
IAN_BOARD = os.getenv("IAN_BOARD")
LIST_ID = os.getenv("LIST_ID")

url = "https://api.trello.com/1/cards?idList=619fcb801249d837919f8965&key=0e26d4796e5d6b6281a4a245b1662644&token=053f6466d9322e4e272f1af322656285cc6c301432678605cb7fef5511947a4a&name=Tenth"

headers = {
    "Accept": "application/json"
}

query = {
    'idList': '5abbe4b7ddc1b351ef961414'
}

response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
)

print(json.dumps(json.loads(response.text),
      sort_keys=True, indent=4, separators=(",", ": ")))


# Redacted ==>
# https://api.trello.com/1/cards?idList={LIST_ID}&key={IAN_KEY}&token={IAN_TOKEN}&name={name}
