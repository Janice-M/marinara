from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

#flask extension instances

login_manager = LoginManager()
login_manager.session_protection = 'strong'
bootstrap = Bootstrap ()
db = SQLAlchemy()
mail= Mail()

#initializing a flask application 

def create_app(config_name)


    app = Flask(__name__)

    from app import views