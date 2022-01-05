from os import name
from flask import Flask, render_template, redirect, request, url_for
from todo_app.trello_items import new_todo, fetch_todo, fetch_in_progress, fetch_done, delete_task
from todo_app.flask_config import Config


app = Flask(__name__)
app.config.from_object(Config())


##########  GET ALL CARDS  ##########
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', fetch_todo=fetch_todo, fetch_in_progress=fetch_in_progress, fetch_done=fetch_done)

##############################################################################################


###########  UPDATE TO-DO  ################
@app.route('/update/<id>', methods=['PUT'])
def update(id):
    update_task(id=request.form['update_id'])
    return redirect(url_for('index'))


###########  NEW TO-DO  ################
@app.route('/new_todo', methods=['POST'])
def new_todo():
    name = request.form['todo']
    new_todo(name)
    return redirect(url_for('index'))


###########  DELETE TO-DO   ##########
@app.route('/remove/<id>', methods=['POST'])
def delete(id):
    delete_task(id=request.form['remove_id'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
