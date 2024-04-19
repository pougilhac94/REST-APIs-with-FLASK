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
>Les variables de configuration peuvent être placées dans 2 fichiers : **.env**
and **.flaskenv**. Le fichier .flaskenv est plutôt utilisé pour les commandes
Flask CLI et .env pour l'application.
>
>>><mark>Dans le cas présent, toutes les variables sont placées dans le fichier .env</mark>
>
>### Instance base de données
>
>L'instance SQLAlchemy est lancée par le module app.py (_application Flask_).
>
>Pour l'exemple, 2 SGBD sont utilisés, chacun pour un environnement particulier :
>
>>>* Développement : **SQLite**
>>>
>>>* Production : **PostgreSQL**
>
>### Docker

**Environnement facultatif tant que l'on ne passe pas par un hébergement sur render.**
>
>>><mark>Si l'on veut passer par Docker, il faut d'abord lancer Docker Desktop.</mark>
>
>Il faut veiller à créer manuellement le fichier _dockerfile_ à la racine du
répertoire de l'application. Il pourra être complété par un fichier _dockerignore_.
>
>* Créer l'image
>
>* Produire le container
>
>>>>Plusieurs options de positionnement de la base de données sont envisageables:
>
>>>>* **Bind Mount** : le chemin d'accès de la base sur le disque dur du PC est
indiqué en dur (chemin complet dans le cas de Windows)  
>>>>* **Volume** : création d'un Volume Docker qui pointera sur un répertoire
donné.  
Cet usage semble le plus pratique, toutefois je n'ai pas réussi à connecter
DBeaver à la BD.
>>>>* Accès sur une base hébergée sur le cloud (illustration avec render).
>
>>>>* En l'absence de toute information, **les données ne seront pas persistentes**
(réinitialisation à chaque mise à jour de l'image).
>
>### Insomnia[^1]
>
>Environnement permettant de tester les APIs. Cet environnement est indépendant
de Flask et ne nécessite donc aucune importation préalable dans l'application
>
>>><mark>Il faut se connecter sur le site
[Insomnia](https://app.insomnia.rest/app/dashboard/organizations)
et ouvrir son espace de travail</mark>

[^1]: Prendre garde au rafraîchissement de token, la variable access_token ne provenant que d'une seul requête d'Insomnia (le login), sa mise à jour par une requête refresh ne sera pas pris en compte.
>
>### Swagger
>
>Environnement _local_ documentaire et permettant de tester les APIs
(environnement associé à la bibliothêque api de _flask_smorest_).
>
>**Il faut se connecter [ici](http://localhost:5000/swagger-ui)**
>
>### JWT I/O
>
>Environnement permettant de tester un JWT
>
>**Il faut se connecter [ici](https://jwt.io)**
>
>### Gunmail
>
>Service de livraison d'e-mails permettant d'envoyer, de recevoir et de suivre
des e-mails.
>
>1. Les mails ne sont envoyés qu'à une seule adresse (la mienne) dans le cadre
d'un service gratuit _(vérifier dossier spam)_.
>
>2. Deux variables d'environnements sont à prendre en compte.
>
>**Le suivi du service est [ici](https://app.mailgun.com/mg/dashboard)**>
>
>### Git
>
>Environnement de partage et de sauvegarde de l'environnement\
>>>L'environnement est créé par la commande `git init`. Il doit être complété
par un fichier _gitignore_.\
>>>Gestion simplifiée par les extensions de VS Code
>
>### Render (_Production_)
>
>Render est un site d'hébergement sur lequel l'application est accessible (mise
à jour à partir du dépôt Git et via Docker).
>
>Il est ici considéré que l'environnement de production est hébergé sur _render_
à la différence de l'environnement de développement qui reste _local_.
>
>>>_Ne pas omettre de charger manuellement les variables d'environnement sur le portail_
>
>### G Unicorn (_Production_)
>
>Serveur web HTTP WSGI écrit en Python et disponible pour Unix.
>Il sera utilisé sur Render en lieu et place du serveur intégré à Flask à usage
purement local sur un docker local
>
>>>_G Unicorn n'a pas à être installé sur la machine virtuelle (niveau local)._
>>>
>>>_G Unicorn doit être mentionné dans le fichier **requirements**._
>
>### Redis (_Production_)
>
>Redis est un système de gestion de base de données clé-valeur extensible,
très hautes performances. il est ici utilisé pour la mise en place et la gestion
d'une file d'attente pour l'envoi des mails.
>
>Redis est ici installé sur Render. Pour s'affranchir de Render, il faudrait
installer Redis localement ou envoyer directement les mails sans passer par
une file d'attente.
>
>La file d'attente peut être gérée directement sous Linux mais pas sous Windows.
Pour Windows, il faut donc passer par Docker.
>
## Organisation
>
>*A COMPLETER*
