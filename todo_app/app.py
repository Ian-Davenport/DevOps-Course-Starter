from os import name
from flask import Flask, render_template, redirect, request, url_for
from todo_app.trello_items import new_todo, fetch_todo, fetch_in_progress, fetch_done, delete_task, move_to_done, move_to_inprog
from todo_app.flask_config import Config


app = Flask(__name__)
app.config.from_object(Config())


##########  GET ALL CARDS  ##########
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', fetch_todo=fetch_todo, fetch_in_progress=fetch_in_progress, fetch_done=fetch_done)

##############################################################################################


###########  MOVE TO DONE  ################
@app.route('/move_to_done/<id>', methods=['POST'])
def mark_done(id):
    move_to_done(id=request.form['complete_id'])
    return redirect(url_for('index'))


###########  MOVE TO IN PROGRESS  ################
@app.route('/move_to_inprog/<id>', methods=['POST'])
def mark_inprog(id):
    move_to_inprog(id=request.form['inprog_id'])
    return redirect(url_for('index'))


###########  NEW TO-DO  ################
@app.route('/new_todo', methods=['POST'])
def add_new_todo():
    # name = request.form['todo']
    new_todo(title=request.form.get('item_name'))
    return redirect(url_for('index'))


###########  DELETE TO-DO   ##########
@app.route('/remove/<id>', methods=['POST'])
def delete(id):
    delete_task(id=request.form['remove_id'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
