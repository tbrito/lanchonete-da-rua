#from utils import get_env_variable
import os

POSTGRES_URL = "localhost:5432" #get_env_variable('POSTGRES_URL')
POSTGRES_USER = "postgres" # get_env_variable('POSTGRES_USER')
POSTGRES_PASSWORD = "postgres" # get_env_variable('POSTGRES_PASSWORD')
POSTGRES_DB = "lanchonetedarua" ##get_env_variable('POSTGRES_DB')



class Config(object):
    DEBUG = False
    TESTING = False
    # SQLAlchemy
    uri_template = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'
    SQLALCHEMY_DATABASE_URI = uri_template.format(
        user=POSTGRES_USER,
        pw=POSTGRES_PASSWORD,
        url=POSTGRES_URL,
        db=POSTGRES_DB)

    # Silence the deprecation warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API settings
    API_PAGINATION_PER_PAGE = 10


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


def get_config(env=None):
    return DevelopmentConfig()