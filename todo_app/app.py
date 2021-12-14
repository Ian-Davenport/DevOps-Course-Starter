from flask import Flask
from flask import render_template, redirect, request
from flask.helpers import url_for
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config
from todo_app.trello_items import fetch_all
import json




app = Flask(__name__)
app.config.from_object(Config())


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



@app.route('/delete_todo', methods=['POST'])
def delete_todo():  
    add_item(title=request.form.get('item_name'))
    return redirect(url_for('index'))  

import requests
import dotenv
import os

dotenv.load_dotenv("../.env")

IAN_KEY=os.getenv("IAN_KEY")
IAN_TOKEN=os.getenv("IAN_TOKEN")
IAN_BOARD=os.getenv("IAN_BOARD")


url = f"https://api.trello.com/1/cards/619fcb801249d837919f8981?key={IAN_KEY}&token={IAN_TOKEN}"



response = requests.delete(url)

print(response.text)




#   json.loads(response.text)   returns json file
# json_response = json.loads(response.text)
# type(json_response)
# <class 'list'>
# response.json()
