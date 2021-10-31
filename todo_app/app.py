from flask import Flask
from flask import render_template


from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html')




# TASKS TO DO:
# Make the app render the index page HTML template.        >>>>>  DONE
# Display the list of saved todo items on the index page. 
# Create a route to add a new todo item to the list.

