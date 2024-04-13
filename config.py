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
    # Par facilité, les variables d'API de courrier sont identiques dans les 2 environnements
    EMAIL_API_KEY = environ.get('MAILGUN_API_KEY') # Service d'email API
    EMAIL_DOMAIN = environ.get('MAILGUN_DOMAIN') # Service d'email API
    REDIS_URL = environ.get('REDIS_URL') # open source, in-memory key-value store (pour gérer la file d'attente)
    

class ProdConfig(Config):
    """Variables propres à la PRODUCTION (inutile si hébergement cloud sur render.com)
    
    Dans le cadre d'un hébergement sur render.com, le fichier .env n'étant pas transmis, ces variables sont chargées manuellement sur le portail Render.
    Cette classe devient alors inutile.
    """
    FLASK_DEBUG = False # redémarre application suite à modification
    SQLALCHEMY_DATABASE_URI = environ.get('PROD__DATABASE_URL') # ou sqlite:///data.db
    JWT_SECRET_KEY = environ.get('PROD_JWT_SECRET_KEY')


class DevConfig(Config):
    """Variables propres au DEVELOPPEMENT
    
    Variable FLASK_DEBUG = True pour mise à jour automatique de l'application FLASK suite à modification de tout fichier
    Si variable DEV_DATABASE_URL absente du fichier .env, la base de données est SQKite par défaut (et en local)
    """
    FLASK_DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URL', 'sqlite:///data.db') # sqlite par défaut
    JWT_SECRET_KEY = environ.get('DEV_JWT_SECRET_KEY')