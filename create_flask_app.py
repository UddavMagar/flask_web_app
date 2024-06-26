import os
import sys

def create_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)

def create_project_structure(project_name):
    base_dirs = [
        f"{project_name}/app",
        f"{project_name}/app/templates",
        f"{project_name}/app/static",
        f"{project_name}/app/static/css",
        f"{project_name}/app/static/js",
        f"{project_name}/app/static/img",
        f"{project_name}/config",
        f"{project_name}/migrations"
    ]

    files = {
        f"{project_name}/app/__init__.py": """
from flask import Flask
from config.config import Config
from app.extensions import db, migrate
from app import routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(routes.bp)

    return app
        """,
        f"{project_name}/app/routes.py": """
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template('index.html')
        """,
        f"{project_name}/app/models.py": """
from app.extensions import db


        """,
        f"{project_name}/app/forms.py": """


        """,
        f"{project_name}/app/extensions.py": """
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
        """,
        f"{project_name}/app/templates/index.html": """
<!doctype html>
<html lang="en">
  <head>
    <title>Flask App</title>
    <style>
    body {
      display: flex; 
      justify-content: center; 
      align-items: center; 
      min-height: 100vh; 
      background-color: #3f17f3;
      background: linear-gradient( #6765F2, #965AF6);
    }

.container {
  position: relative;
  width: 800px;
  height: 300px;
  transition: 200ms;
  align-items: center;
}


#card {
  position: absolute;
  inset: 0;
  z-index: 0;
  display: flex;
  padding-left: 20px;
  padding-top: 100px;
  border-radius: 20px;
  background: #4C3BCF;
}

h1{
 
  left: 30px;
  font-size: x-large;
  font-weight: bold;
  color: white;
}
h4{
 left: 30px;
 font-weight: bold;
 color: white;
}


.card1 {
  position: absolute;
  bottom: 50px;
  left: 100px;
  width: 320px;
  height: 50px;
  padding: 10px;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size:xx-large;
  font-weight: bold;
  color: white;
  backdrop-filter: blur(30px);
  box-shadow: 0px 0px 30px rgba(227, 228, 237, 0.37);
  border: 1.5px solid rgba(255, 255, 255, 0.18);
}

    </style>
  </head>
  <body>
    <div class="container">
        <div id="card">
        <h1>Build Your First Web Application</h1>
        <div class="card1">
         Python and Flask
      </div>  
        </div>
    </div>
  </body>
  </html>
        """,
        f"{project_name}/config/config.py": """
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Uncomment the database configuration you prefer to use

    # SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'

    # MySQL
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'

    # PostgreSQL
    # SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/db_name'

    # MongoDB
    # MONGODB_SETTINGS = {
    #     'db': 'myDatabase',
    #     'host': 'localhost',
    #     'port': 27017
    # }

    SQLALCHEMY_TRACK_MODIFICATIONS = False
        """,
        f"{project_name}/requirements.txt": """
Flask
Flask-SQLAlchemy
flask_migrate
#flask_bcrypt
#flask_wtf
#flask_login
#email-validator
#pymysql  # For MySQL
#psycopg2  # For PostgreSQL
#pymongo  # For MongoDB
        """,
        f"{project_name}/.gitignore": """
venv/
__pycache__/
*.pyc
instance/
.webassets-cache
.env
.venv
        """,
        f"{project_name}/README.md": f"# {project_name.capitalize()}\n\n## Description\n\nYour app is ready to be used\n",
        f"{project_name}/run.py": """
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
        """
    }

    for directory in base_dirs:
        os.makedirs(directory, exist_ok=True)

    for file_path, file_content in files.items():
        create_file(file_path, file_content.strip())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_flask_project.py project_name")
    else:
        project_name = sys.argv[1]
        create_project_structure(project_name)
        print(f"Project {project_name} created successfully.")
