# flask_web_app

# Flask Project Template

## Description

This template sets up a basic Flask web application with a structured project layout, including configurations for using SQLAlchemy for database interactions and Flask-Migrate for database migrations.

## How to Run

### Step 1: Get the Python file

### Git

Clone this repository
```sh
$ git clone https://github.com/UddavMagar/flask_web_app.git
```

### Step 2: Run the Python file

To create your project, run the following command in your terminal:

```sh
$ cd flask_web_app
$ python create_flask_project.py <your_project_name> # Give name you want for your project.
```

### Step 3: Navigate to the Project Folder
Go to the newly created project folder: 

```sh
$ cd <your_project_name>
```


### Step 4: Create and Activate a Virtual Environment
Create a virtual environment in the project folder and activate it:

On Windows:

```sh
$ python -m venv venv
$ venv\Scripts\activate
```

On macOS/Linux:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

### Step 5: Install Requirements
Install the required packages listed in requirements.txt:

```sh
$ pip install -r requirements.txt
```

### Step 6: Run the Flask Application
Run the application:

```sh
$ python run.py
```
You should see your Flask web application running, where you can start building and expanding your structured Flask app.

## To Initialize and Migrate the Database
To initialize your database, use the following command:

```sh
$ flask db init
```
To migrate your database, use the following commands:
```sh
$ flask db migrate
$ flask db upgrade
```
Whenever you make changes to your models, run these commands to apply the changes to your database smoothly.



