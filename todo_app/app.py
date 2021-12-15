
from flask import Flask, render_template, redirect, request, url_for
# from flask_bootstrap import Bootstrap
# def create_app():
#   app = Flask(__name__)
#   Bootstrap(app)
#   return app
# from flask.helpers import url_for
# from todo_app.flask_config import Config
from todo_app.trello_items import fetch_todo, fetch_in_progress, fetch_done, delete_task
# import json
# import requests
# import dotenv
# import os


# dotenv.load_dotenv("../.env")


from todo_app.flask_config import Config
app = Flask(__name__)
app.config.from_object(Config())


# IAN_KEY = os.getenv("IAN_KEY")
# IAN_TOKEN = os.getenv("IAN_TOKEN")
# IAN_BOARD = os.getenv("IAN_BOARD")


##########  GET ALL CARDS  ##########
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', fetch_todo=fetch_todo, fetch_in_progress=fetch_in_progress, fetch_done=fetch_done)


# url = "https://api.trello.com/1/boards/{id}/cards"
# url = "https://api.trello.com/1/boards/{id}/lists"

# response = requests.request("GET", url)
# print(response.text)


# #########  THIS IS JUST THE 'TO DO' LIST  ##########
# @app.route('/todo', methods=['POST'])
# def add_todo():
#     add_item(title=request.form.get('item_name'))
#     return redirect(url_for('index'))


# ##########  DELETE  ##########
@app.route('/remove/<id>', methods=['POST'])
def delete(id):
    delete_task(id=request.form['remove_id'])
    return redirect(url_for('index'))

# response = requests.delete(url)

# @app.route('/add/', methods=['POST'])
# def add():
#     add_task(title=request.form.get('item_name'))
#     return redirect(url_for('index'))


###########  MOVE CARD TO 'IN PROGRESS'  #############
# @app.route('/move_to_in_progress', methods=['POST'])
# def move_to_in_progress():
#     add_item(title=request.form.get('item_name'))
#     return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
