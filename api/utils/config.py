import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "mysql+pymysql://")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/jsonx"
    SQLALCHEMY_ECHO = False

# "mysql+pymysql://qonclhz38vuc5vw0:k99qvyi1uem9scbh@otmaa16c1i9nwrek.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/fkh7jc7hbhc8fe4a"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "mysql+pymysql://root:root@localhost/jsonx")
    SQLALCHEMY_ECHO = False
