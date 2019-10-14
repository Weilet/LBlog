from flask import Flask, render_template
from config import config
from extensions import *
from LBlog.auth import auth_bp
from LBlog.blog import blog_bp


def register_extension(app):
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    migrate.init_app(app, db)


def creat_app(config_name):
    """
    init all extension of the app
    configure environment for the app
    :param config_name: String, name of configuration
    :return: app: Flask app
    """
    app = Flask(__name__)
    config[config_name].init_app(app)
    app.config.from_object(config[config_name])
    register_bp(app)
    register_extension(app)
    register_error_handle(app)
    return app


def register_bp(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(blog_bp)


def register_error_handle(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html')


# TODO: refactor template with pjax
# TODO: add a confirmation before deletion
