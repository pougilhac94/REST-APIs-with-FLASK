Instance SQLAlchemy
===================

BD de développement : SQLite
------------------------------

    Les données sont placées dans le fichier **sqlite_stores.db** du dossier **instance**.

    Le nom de la base de données est ici fixé par la valeur du paramètre **SQLALCHEMY_DATABASE_URI** qui a pris par défaut la valeur **sqlite:///dataname.db** dans le fichier **config.py** et où *dataname* est le nom attribué à la base de données.

    La creation initiale de la base de données est liée aux commandes successives dans *app.py* :

        db = SQLAlchemy() *dans db.py*

        db.init_app(app) *où app = flask(__name__)*
        
        with app.app_context():

            db.create_all()

BD de production : PostgreSQL
--------------------------------

    Les données sont hébergées sur **render.com**

Visualisation de la base de données : DBeaver
--------------------------------------------------------------------------

    Logiciel permettant l'administration et le requêtage de base de données.

    Utilisable sur les 2 BD sans que l'application Flask soit lancée.

Fichier db.py 
-------------

    Après l'import de *SQLAlchemy* à partir de *flask_sqlalchemy*, l'instance SQLAlchemy créée par SQLAlchemy() donne accès à la classe *db.Model*_* pour définir les modèles, et à *db.session* pour le requettage.

    See app.py for the parameters

----

.. automodule:: db
    :members: