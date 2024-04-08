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
* Création de l'image rest-apis-flask-python :\
  *à partir du terminal, saisir le . final pour répertoire courant de l'image*\
```docker build -t flask-smorest-api .```[^1]\
```docker run -dp 5000:5000 -w /app -v absolute-path:/app" flask-smorest-api```[^2]
>
>*NB : Pas d'utilisation d'un **Docker Volume** mais plutôt d'un **Bind Mounts***

### Environnement de production sur Render avec G Unicorn

* Script :\
```FROM python:3.11```\
```WORKDIR /app```\
```COPY requirements_new.txt .```\
```RUN pip install --no-cache-dir --upgrade -r requirements_new.txt```\
```COPY . .```\
```CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]```
>
[^1]: *-t* pour tagué l'image avec *flask-smorest-api*

[^2]: *-w /app* - sets the container's present working directory where the command will run from\
*-v "/c/users....:/app"* - bind mount (link) the host's present getting-started/app directory to the container's /app directory.

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
