class DevConfig(object):
    SECRET_KEY = 'book-publishing-app'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:josh730@127.0.0.1:3306/bookpublishingapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
