# Avant-propos

## Sphinx

Pour générer la documentation HTML :

>>>`.\/docs/make.bat html`
>
>* [Tutoriel](https://techwritingmatters.com/documenting-with-sphinx-tutorial-intro-overview>)

## Environnements

>### Environnement virtuel
>
>>>`.\/.venv/scripts/activate.bat`
>>>
>>>`.\/.venv/scripts/deactivate.bat`
>
>### Flask
>
>Lancement direct en ligne de commande : `flask run` (_ou passer par Docker_)
>
>Les variables de configuration peuvent être placées dans 2 fichiers : **.env** and **.flaskenv**. Le fichier .flaskenv est plutôt utilisé pour les commandes Flask CLI et .env pour l'application.
>
>>><mark>Dans le cas présent, toutes les variables sont placées dans le fichier .env</mark>

>### Instance base de données
>
>L'instance SQLAlchemy est lancée par le module app.py (_application Flask_)
>
>### Docker
>
>>><mark>Si l'on veut passer par Docker, il faut d'abord lancer Docker Desktop.</mark>
>
>Il faut veiller à créer manuellement le fichier _dockerfile_ à la racine du répertoire de l'application. Il pourra être complété par un fichier _dockerignore_.
>
>* Créer l'image
>
>>>`docker build -t flask-smorest-api .`
>
>* Produire le container
>
>>>`docker run -dp 5000:5000 -w /app -v "/c/users/christian/documents/udemy/recording:/app" flask-smorest-api`
>>>
>>>(_cette commande lance l'application Flask sur le port 5000_)
>
>### Insomnia[^1]
>
>Environnement permettant de tester les APIs. Cet environnement est indépendant de Flask et ne nécessite donc aucune importation préalable dans l'application
>
>>><mark>Il faut se connecter sur le site [Insomnia](https://app.insomnia.rest/app/dashboard/organizations) et ouvrir son espace de travail</mark>

[^1]: Prendre garde au rafraîchissement de token, la variable access_token ne provenant que d'une seul requête d'Insomnia (le login), sa mise à jour par une requête refresh ne sera pas pris en compte.
>
>### Swagger
>
>Environnement _local_ documentaire et permettant de tester les APIs (environnement associé à la bibliothêque api de _flask_smorest_).
>
>**Il faut se connecter [ici](http://localhost:5000/swagger-ui)**
>
>### JWT I/O
>
>Environnement permettant de tester un JWT
>
>**Il faut se connecter [ici](https://jwt.io)**
>
## Organisation
>
>*A COMPLETER*
