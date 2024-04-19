Dossier Migrations
==================

Historique des versions de la base de données.

    Pour gérer les migrations, il faut ajouter dans app.py:
            migrate = Migrate(app, db)
            
        et supprimer :

            db.create_all()

    En lignes de commande pour la base locale SQLite :

        **flask db migrate** *ajout dossier migration*

        supprimer la base de données (dans dossier instance)

        **flask db migrate** *toujours vérifier le dossier .py dans le sous-dossier versions de migrations*

        **flask db update** ou flask db **downgrade** selon le but recherché

*En cas de difficultés dans le versionning, il peut être utile de passer la commande*

    *db stamp head*