Instance SQLAlchemy
===================

BD de développement : SQLite
------------------------------

    Les données sont placées dans le fichier **data.db** du dossier **instance**.

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