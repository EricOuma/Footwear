import os
import cloudinary

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()
cloudinary = cloudinary

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    # Find out why config_name does not work here
    app.config.from_object(app_config[os.getenv('FLASK_ENV')])
    app.config.from_pyfile('config.cfg')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)
    
    cloudinary.config(
      cloud_name = app.config['CLOUDINARY_CLOUD_NAME'],
      api_key = app.config['CLOUDINARY_API_KEY'],
      api_secret = app.config['CLOUDINARY_API_SECRET']
      )


    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

        
    return app
