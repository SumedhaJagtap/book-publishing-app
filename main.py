from flask import Flask

from flask_sqlalchemy import SQLAlchemy


from app import create_app,db
from app.config.dev import DevConfig
from app.auth.models import User

if __name__ == '__main__':
    flask_app = create_app(DevConfig)
    with flask_app.app_context():
        db.create_all()
        
    flask_app.run(debug=True)
