
from flask import Flask, render_template, redirect, request, url_for
from todo_app.trello_items import fetch_list, new_todo, delete_task, move_to_done, move_to_inprog
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def to_do_items(self):
        to_do_output = []
        for item in self._items:
            if item.status == "To-Do":
                to_do_output.append(item)
        return to_do_output

    @property
    def doing_items(self):
        doing_output = []
        for item in self._items:
            if item.status == "In Progress":
                doing_output.append(item)
        return doing_output

    @property
    def done_items(self):
        done_output = []
        for item in self._items:
            if item.status == "DONE!":
                done_output.append(item)
        return done_output


@app.route('/', methods=['GET'])
def index():
    items = fetch_list()
    item_view_model = ViewModel(items)
    
    return render_template('index.html', view_model=item_view_model)


@app.route('/new_todo', methods=['POST'])
def add_new_todo():
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
