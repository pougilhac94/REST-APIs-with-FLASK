Application FLASK
=================

* Pour créer l'application Flask, le module app.py s'appuie principalement sur :

    - **Flask**

    - **flask_smorest : Api** (classe permettant de créer des REST API avec Flask)
    
    - **flask_jwt_extended : JWTManager** (classe permettant de générer et de vérifier les jetons JWT (Json Web Token)).

* au sein du projet :

    - **db** : instance SQLAlchemy

    - **blocklist** : liste des tokens bloqués

    - **Blueprint** : pour chaque ressource


* Instance **SQLAlchemy**

    - **Callback init_app()** used to initialize an application for the use with the database setup.

    - **Method create_all()** tpour créer les tables.

        This method will issue queries that first check for the existence of each individual table, and if not found will issue the CREATE statements.

        create_all() creates foreign key constraints between tables usually inline with the table definition itself, and for this reason it also generates the tables in order of their dependency. 

    - **Migrate** pour prendre en compte tout changement de schéma de la base de données, et pour changer de SGBD (SQLite à PostgreSQL par exemple).
    
        La méthode create_all est alors abandonée.

        * pour une migration : **flask db.migrate**

        * pour une mise à jour : **flask db.upgrade**
        
        NB : La base de données est réinitialisée lors de la première migration.

* Création objet **Api()**

* Création objet **JWTManager()**

.. tip::
       Pour la gestion des variables d'environnement décrites dans le fichier **.env**, app.py s'appuie sur le fichier **config.py** par appel de **config.from_object** en précisant l'environnement de travail (développement ou production).

---

.. automodule:: app
    :members: 