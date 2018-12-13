from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin

#initialization of the database
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

migrate=Migrate(app,db)
admin = Admin(app,template_mode='bootstrap3')

from app import views, models
