from os import name
from flask import Flask, render_template, redirect, request, url_for
from todo_app.trello_items import new_todo, fetch_todo, fetch_in_progress, fetch_done, delete_task, move_to_done, move_to_inprog
from todo_app.flask_config import Config


app = Flask(__name__)
app.config.from_object(Config())


##########  GET ALL CARDS  ##########
@app.route('/', methods=['GET'])
def index():
    tasks = fetch_todo()
    in_progress_tasks = fetch_in_progress()
    done_tasks = fetch_done()
    return render_template('index.html', tasks=tasks, in_progress_tasks=in_progress_tasks, done_tasks=done_tasks)

##############################################################################################


@app.route('/new_todo', methods=['POST'])
def add_new_todo():
    # name = request.form['todo']
    new_todo(title=request.form.get('item_name'))
    return redirect(url_for('index'))


@app.route('/move_to_inprog/<id>', methods=['POST'])
def mark_inprog(id):
    move_to_inprog(id=request.form['inprog_id'])
    return redirect(url_for('index'))


@app.route('/move_to_done/<id>', methods=['POST'])
def mark_done(id):
    move_to_done(id=request.form['complete_id'])
    return redirect(url_for('index'))


@app.route('/remove/<id>', methods=['POST'])
def delete(id):
    delete_task(id=request.form['remove_id'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
