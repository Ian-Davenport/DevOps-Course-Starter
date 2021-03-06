# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

#### Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

#### RUNNING THE APP
Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit (http://localhost:5000/) in your web browser to view the app.


Please follow these steps in order to run the project:
- Sign into Trello or create a Trello account
- Generate a Key
- Generate a Token
- Declare your Key & Token in the .env file


# TESTING
A testing secion can be found in the code named 'test_app.py'.
Three unit tests have been created.

To check on the testing, please run:
$ poetry run pytest

The tests are to establish the three lists used in the app ("To Do", "In Progress" & "Done") will only show their own items only.


# ANSIBLE
Log-on to your Controller Node and run the following to provision the host VM:

$ ansible-playbook playbook -i Inventory

Ensure you can reach your Host VM via SSH for this to run successfully.


# DOCKER

** You will need to have the Docker Desktop app installed to run the following section.
** Visit https://www.docker.com/products/docker-desktop/ to download and install.


##### To BUILD then RUN the Production environment, enter each of the following two lines separately into the terminal and hit 'Enter' after each one:

#### To run PRODUCTION container
1. $ docker build --target production --tag todo-app:prod .
2. $ docker run -p 80:80 --env-file .env todo-app:prod

** To see the above running, open your browser and type the following in the address bar: localhost:80


#### To BUILD then RUN the Development environment, enter the following two lines separately into the terminal and hit 'Enter' after each one:
#### To run DEVELOPMENT container
1. $ docker build --target development --tag todo-app:dev .
2. $ docker run -p 5000:5000 --env-file .env todo-app:dev

** To see the above running, open your browser and type the following in the address bar: localhost:5000 

#### However to simplify the build & run process, a yaml file has been created which contains all the instructions meeded to build and run both containers and saves you having to enter the long codes.
**  To use this feature, in the terminal simply type: 
1. $ docker-compose up


#### HEROKU ####
This is the Module_8 project exercise.
https://todo-app-ian-module-8.herokuapp.com/

Exercise feedback:
Fixed issue whereby Heroku was creating a new container each time.
On 'my-ci-pipeline.yml' line 48:  This was: heroku_app_name:"ian-module-8"
    Changed to: heroku_app_name:"todo-app-ian-module-8"
Established Heroku was creating a new container due to line 48. Resolved.


#### AZURE ####
For Module_9 project exercise we carried on from last time, but rather than have 
Docker publish to Heroku, this time Docker published to Azure instead. 

=======
