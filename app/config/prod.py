from app.config import Config

class ProdConfig(Config):
    DEBUG = False
    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:josh730@127.0.0.1:3306/bookpublishingapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
