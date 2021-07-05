import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = False
    CRRF_ENABLED = True
    SECRET = os.environ.get("SECRET")
    UPLOAD_FOLDER = os.environ.get("static")


class DevelopmentConfig(Config):
    DEBUG = True
    #Load  sql Datgabase configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False










