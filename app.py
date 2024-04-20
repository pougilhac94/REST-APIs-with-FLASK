from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask import jsonify
from flask_migrate import Migrate
# import redis
# from rq import Queue

from flask import render_template

from db import db
from blocklist import BLOCKLIST

from ressources.item import blp as ItemBlueprint
from ressources.store import blp as StoreBlueprint
from ressources.tag import blp as TagBlueprint
from ressources.user import blp as UserBlueprint

def create_app(db_url=None):
    """Création de l'application Flask
    
    Récupération des paramètres de configuration dans config.py

    Pour le fun, appel de la page du portail (index.html)

    Etablissement de la connexion avec Redis et mise en place de la file d'attente

    Migration (si nécessaire) de la base de données
    
    Gestion des APIs et des tokens (JWT)    

    Chargement des différents Flask Blueprint à partir du dossier Ressources:
        - item
        - store
        - tag
        - user

    Args:
        db_url (optional): Defaults to None.

    Returns:
        object: application Flask 

    Fonctions imbriquées:
        check_if_token_in_blocklist

        revoked_token_callback

        expired_token_callback

        invalid_token_callback

        imissing_token_callback

    """
    app = Flask(__name__)

    # Usage de la configuration de production (inutile si hébergement cloud via)
    #app.config.from_object('config.ProdConfig')

    # Usage de la configuration de développement
    app.config.from_object('config.DevConfig')
  
    # 3 lignes pour afficher une page de garde de l'appli Flask (voir templates/index.html)
    @app.route('/')
    def home():
        return render_template('index.html')

    # Etablissement de la file d'attente pour l'envoi des mails (plutôt qu'un envoi direct)
    # my_redis_url = app.config.get("REDIS_URL")# Get this from Render.com or run in Docker
    # connection = redis.from_url(my_redis_url)
    # print(f"APP.PY - {my_redis_url=} pour lancement queue", flush=True)
    # app.queue = Queue("emails", connection=connection)

    #This callback used to initialize an application for the use with this database setup.
    db.init_app(app)

    # Migration de la base (faire un delete avant et supprimer le create_all)
    migrate = Migrate(app, db)
    api = Api(app)
    
    jwt =JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        """
        Check if token is in blocklist

        Args:
            jwt_header 
            jwt_payload

        Returns:
            bool
        """
        return jwt_payload["jti"] in BLOCKLIST
    
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        """Callback de token révoqué

        Args:
            jwt_header
            jwt_payload

        Returns:
            error: 401
            dict: message et error
        """
        return (
            jsonify(
                {"description": "Token révoqué.", "error": "token_revoked"}
            ),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        """Callback de token frais requis

        Args:
            jwt_header
            jwt_payload

        Returns:
            error: 401
            dict: message et error
        """
        return (
            jsonify(
                {"description": "Token pas frais.", "error": "fresh_token_required"}
            ),
            401,
        )

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        """Callback de token expiré

        Args:
            jwt_header
            jwt_payload

        Returns:
            error: 401
            dict: message et error
        """
        return (
            jsonify({"message": "Token expiré",
                      "error": "token_expired"}),
            401
        )
            
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        """callback de token invalide

        Args:
            error

        Returns:
            error: 401
            dict: message et error
        """
        return (
            jsonify({"message": "La vérification de la signature a échouée",
                      "error": "invalid_token"}),
            401
        )

    @jwt.unauthorized_loader
    def imissing_token_callback(error):
        """callback de token absent

        Args:
            error

        Returns:
            error: 401
            dict: message et error
        """
        return (
            jsonify({"description": "Token requis absent",
                      "error": "authorisation_required"}),
            401
        )

    # ## Method create_all() to create tables with SQLAlchemy. (usage unique)
    # with app.app_context():
    #    db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)

    return app

create_app()