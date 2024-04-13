Configuration de l'application Flask
====================================

- Le fichier **config.py** permet de faire le lien entre **app.py**, les variables de configuration sont placées dans **.env** et appelées comme suit :

    * app.config(*nom_variable*)

- Ces variables sont accessibles dans d'autres fichiers après avoir chargé préalablement la bibliothêque Flask **current_app**, les variables sont alors appelées 

    * **current_app**.config(*nom_variable*)

----

.. automodule:: config
    :members:
