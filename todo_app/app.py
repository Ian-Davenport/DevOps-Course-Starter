from flask import Flask
from flask import render_template, redirect, request
from flask.helpers import url_for
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods=['GET'])
def index():
    items = get_items()
    return render_template('index.html', get_items=get_items)



@app.route('/todo', methods=['POST'])
def add_todo():  
    add_item(title=request.form.get('item_name'))
    return redirect(url_for('index'))  



