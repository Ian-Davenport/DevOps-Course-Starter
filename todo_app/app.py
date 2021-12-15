from flask import Flask
from flask import render_template, redirect, request
# from flask_bootstrap import Bootstrap
# def create_app():
#   app = Flask(__name__)
#   Bootstrap(app)
#   return app
from flask.helpers import url_for
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config
from todo_app.trello_items import fetch_all
import json
import requests
import dotenv
import os
from flask import Flask

dotenv.load_dotenv("../.env")


app = Flask(__name__)
app.config.from_object(Config())


IAN_KEY = os.getenv("IAN_KEY")
IAN_TOKEN = os.getenv("IAN_TOKEN")
IAN_BOARD = os.getenv("IAN_BOARD")


# @app.route('/', methods=['GET'])
# def index():
#     items = get_items()
#     return render_template('index.html', get_items=get_items)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', fetch_all=fetch_all)


@app.route('/todo', methods=['POST'])
def add_todo():
    add_item(title=request.form.get('item_name'))
    return redirect(url_for('index'))


##########  DELETE  ##########
@app.route('/delete_todo', methods=['POST'])
def delete_todo():
    add_item(title=request.form.get('item_name'))
    return redirect(url_for('index'))


CARD = "619fcb801249d837919f8981"
url = f"https://api.trello.com/1/cards/{CARD}?key={IAN_KEY}&token={IAN_TOKEN}"
response = requests.delete(url)


###########  MOVE CARD TO 'DONE' LIST #############
@app.route('/move_to_done', methods=['POST'])
def move_to_done():
    add_item(title=request.form.get('item_name'))
    return redirect(url_for('index'))

CARD = "61a52ac8fd1f723a75eeddb1"
DONE_LIST = "619fcb801249d837919f8968"
url = f"https://api.trello.com/1/cards/{CARD}?idList={DONE_LIST}&key={IAN_KEY}&token={IAN_TOKEN}"
response = requests.delete(url)


###########  MOVE CARD TO 'IN PROGRESS'  #############
@app.route('/move_to_in_progress', methods=['POST'])
def move_to_in_progress():
    add_item(title=request.form.get('item_name'))
    return redirect(url_for('index'))

CARD = "61a66358d56e1381cb97f284"
IN_PROGRESS = "619fcb801249d837919f8966"
url = f"https://api.trello.com/1/cards/{CARD}?idList={IN_PROGRESS}&key={IAN_KEY}&token={IAN_TOKEN}"


response = requests.put(url)
print(response.text)


# json.loads(response.text)   returns json file
# json_response = json.loads(response.text)
# type(json_response)
# <class 'list'>
# response.json()
