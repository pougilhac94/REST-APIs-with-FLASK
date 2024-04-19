# Environnement Docker

>>>><mark>NE PAS OUBLIER DE LANCER DOCKER DESKTOP</mark>

## Fichier : Dockerfile

### Environnement de développement

* Image de base\
```FROM python:3.11```
>
* Port de l'applicatiobn flask : 5000\
```EXPOSE 5000```
>
* Répertoire dans l'image Docker\
```WORKDIR /app```
>
>NB : commande pour connaître la liste complète des modules installés\
```pip freeze > requirements.txt```

* Copie des nouveaux modules à installer  dans le répertoire courant de l'image\
```COPY requirements_new.txt .```
>
* Plutôt que de préciser quels fichiers installer, requirements.txt suffit\
```RUN pip install -r requirements_new.txt```
>
* Copie du répertoire courant dans le répertoire courant de l'image\
```COPY . .```\
```CMD ["flask", "run", "--host", "0.0.0.0"]```
>
* Création de l'image rest-api-recording-email :  
  *à partir du terminal, saisir le . final pour répertoire courant de l'image*  
```docker build -t rest-api-recording-email .```[^1]
>
* Lancement du container
  * Plusieurs options de positionnement de la base de données sont envisageables:
    * basic container pour une image :
```docker run -dp 5000:5000 -w /app rest-api-recording-email```[^2]
    * Lancement du container avec la BD sur le DD (**Bind Monts**):>  
```docker run -dp 5000:5000 -v "absolute-path:/app/instance" rest-api-recording-email sh -c "flask run --host 0.0.0.0"```[^2]
    * Lancement du container avec la BD sur un **Volume**:  
```docker run -dp 5000:5000 -v volume_name:/app/instance rest-api-recording-email sh -c "flask run --host 0.0.0.0"```
  * **Bind Mount** : le chemin d'accès de la base est indiqué en dur (chemin complet
dans le cas de Windows)  
```docker run -dp 5000:5000 -w /app -v "/c/users/christian/documents/udemy/recording/instance:/app/instance" rest-api-recording-email```
  * **Volume** : après sa création, le Volume Docker pointe sur un répertoire donné au lancement du run.  
```docker run -p 5000:5000 -v sqlite-stores:/app/instance rest-api-recording-email sh -c "flask run --host 0.0.0.0"```\
La liaison avec le volume créé précédemment est : ```-v volume_name:répertoire```
Cet usage semble le plus pratique, toutefois je n'ai pas réussi à connecter
DBeaver à la BD.
>
* En l'absence de toute information, **les données ne seront pas persistentes**.
>>
>>**WARNING**
>>
>> Sous Windows, il faut passer par Docker pour mettre en oeuvre une *file d'attente*.

### Environnement de production sur Render avec G Unicorn

* Script :\
```FROM python:3.11```\
```WORKDIR /app```\
```COPY requirements_new.txt .```\
```RUN pip install --no-cache-dir --upgrade -r requirements_new.txt```\
```COPY . .```\
```CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]```

* Evolution du script pour automatiser la mise à jour du schéma des tables
>>
>>La ligne ```CMD``` devient :
>>
```CMD ["/bin/bash", "docker-entrypoint.sh"]```
>>
>>sous réserve d'avoir créer préalablement le fichier **docker-entrypoint.sh** :
>>
```flask db upgrade```\
```exec gunicorn --bind 0.0.0.0:80 "app: create_app()"```
>>
[^1]: *-t image_name* pour taguer l'image

[^2]: *-w /app* - sets the container's present working directory where the command will run from  
*-v "/c/users....:/app"* - bind mount (link) the host's present getting-started/app directory to the container's /app directory.  
*-d* - exécution en arrière-plan (d=detach)  
*-p host:container* - adresse du host : port du container (p=publish)

## Fichier .dockerignore

Liste des dossiers que Docker doit ignorer (machine virtuelle python, environnement...)

## Autres commandes

* Liste des containers\
```docker ps```
>
* STOP container\
```docker stop <container_id>```
>
* REMOVE\
```docker rm <container_id>```
