from flask import Flask
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
ckeditor = CKEditor()
migrate = Migrate()


def creat_app(config_name):
    """
    init all extension of the app
    configure environment for the app
    :param config_name: String, name of configuration
    :return: app: Flask app
    """
    app = Flask(__name__)
    # environmental varies configuration
    config[config_name].init_app(app)
    app.config.from_object(config[config_name])
    # extension initialization
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    migrate.init_app(app, db)
    return app


