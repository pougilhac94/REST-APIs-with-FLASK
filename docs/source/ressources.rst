Dossier Ressources
==================

Chaque ressource correspond à un ensemble de classes décrivant les différentes **APIs** sous forme de fonctions.

Toute API s'appuie sur la classe **MethodView** [1]_

Certaines APIs sont amenées à s'appuyer sur des tokens (**JWT**).

Chaque ressource initialise un **Blueprint** [2]_ qui sera par la suite importé dans app.py

Chaque ressource importe préalablement :

    Concernant l'instance SGBD

        les modèles et schémas nécessaires 
        
        l'instance **SQLAlchemy**

.. [1] MethodView is a class within the flask.views module of the Flask project. MethodView is a Python Metaclass that determines the methods, such as GET, POST, PUT, etc, that a view defines.

.. [2] The basic concept of blueprints is that they record operations to execute when registered on an application. Flask associates view functions with blueprints when dispatching requests and generating URLs from one endpoint to another.

----

Une ressource supplémentaire est particulière, il s'agit de **tasks.py** qui a été ajouté pour traiter l'envoi de mail en file d'attente.

La file d'attente étant gérée indépendamment de l'application Flask (l'application ne lance que la file d'attente), ce fichier contient les fonctions de production de mail mais aussi le chargement de variables d'environnement.

----

.. automodule:: ressources.item
    :members:
.. automodule:: ressources.store
    :members:
.. automodule:: ressources.tag
    :members:
.. automodule:: ressources.user
    :members: