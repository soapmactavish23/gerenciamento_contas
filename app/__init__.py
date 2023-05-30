from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

ma = Marshmallow(app)

mi = Migrate(app, db)

from .models import conta_model