import os 
from app.config import Config

class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'book-publishing-app'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
