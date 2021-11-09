from flask import Flask
from flask import render_template
from todo_app.data.session_items import get_items
from todo_app.flask_config import Config


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', get_items=get_items)
    
    

@app.route('/todo', methods=['GET', 'POST'])
def add_todo():
   return render_template('todo.html', get_items=get_items)
 

# TASKS TO DO:
# Make the app render the index page HTML template.        >>>>>  DONE
# Display the list of saved todo items on the index page.  >>>>>  DONE
# Create a route to add a new ToDo item to the list.       >>>>>  DONE ish 

