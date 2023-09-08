# app/__init__.py
from datetime import datetime
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'auth_bp.signin_user'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()


def create_app(config_type):  # test,dev,prod
    app = Flask(__name__)
    app.config.from_object(config_type)
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.catalog import catalog_bp
    app.register_blueprint(catalog_bp)
    from app.auth import auth_bp
    app.register_blueprint(auth_bp)
    return app
