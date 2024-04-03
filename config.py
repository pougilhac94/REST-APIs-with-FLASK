"""
- Import de la bibliothêque dotenv pour lire le fichier **.env**
"""
from os import environ, path
from dotenv import load_dotenv

# Specificy a `.env` file containing key/value config values
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    """Variables communes à tous les environnements"""
    FLASK_APP = "app" # pour appeler le fichier app.py
    PROPAGATE_EXCEPTIONS = True
    API_TITLE =  environ.get('API_TITLE')
    API_VERSION = environ.get('API_VERSION')
    OPENAPI_VERSION = "3.1.0"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProdConfig(Config):
    """Variables propres à la PRODUCTION"""
    FLASK_DEBUG = False # redémarre application suite à modification
    SQLALCHEMY_DATABASE_URI = environ.get('PROD__DATABASE_URI')
    JWT_SECRET_KEY = environ.get('PROD_JWT_SECRET_KEY')


class DevConfig(Config):
    """Variables propres au DEVELOPPEMENT
    
    Variable FLASK_DEBUG = True pour mise à jour automatique de l'application FLASK suite à modification de tout fichier
    """
    FLASK_DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')
    JWT_SECRET_KEY = environ.get('DEV_JWT_SECRET_KEY')