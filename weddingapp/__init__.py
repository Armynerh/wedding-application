from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from weddingapp import config

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")
app.config.from_object(config.Live_config)
csrf = CSRFProtect(app)

db =SQLAlchemy(app)
from weddingapp import models, forms
from weddingapp.routes import admin_routes, user_routes



#import anything that would be used site-wide/globally