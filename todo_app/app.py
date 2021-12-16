
from flask import Flask, render_template, redirect, request, url_for
from todo_app.trello_items import add_task, fetch_todo, fetch_in_progress, fetch_done, delete_task
from todo_app.flask_config import Config
app = Flask(__name__)
app.config.from_object(Config())


##########  GET ALL CARDS  ##########
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', fetch_todo=fetch_todo, fetch_in_progress=fetch_in_progress, fetch_done=fetch_done)


###########  UPDATE CARD  ################
@app.route('/update/<id>', methods=['PUT'])
def update(id):
    update_task(id=request.form['update_id'])
    return redirect(url_for('index'))


###########  ADD CARD  ################
@app.route('/add/', methods=['POST'])
def add():
    add_task(title=request.form.get("item_name"))
    return redirect(url_for('index'))


###########  DELETE  ##########
@app.route('/remove/<id>', methods=['POST'])
def delete(id):
    delete_task(id=request.form['remove_id'])
    return redirect(url_for('index'))


###########  MOVE CARD TO 'IN PROGRESS'  #############
# @app.route('/move_to_in_progress', methods=['POST'])
# def move_to_in_progress():
#     add_item(title=request.form.get('item_name'))
#     return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
