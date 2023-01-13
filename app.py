from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_pyfile('config.py')


db = SQLAlchemy(app)

from models import *

Migrate(app, db)

from views import *

if __name__ == "__main__":
    app.run()
