# Image de base
FROM python:3.11
# port de l'applicatiobn flask : 5000
EXPOSE 5000
# Répertoire dans l'image Docker
WORKDIR /app

# NB : commande pour connaître la liste complète des modules installés
# pip freeze > requirements.txt  

# Copy des nouveaux modules à installer  dans le répertoire courant de l'image
COPY requirements_new.txt .
# Plutôt que de préciser quels fichiers installer, requirements.txt suffit
RUN pip install -r requirements_new.txt
# Copy du répertoire courant dans le répertoire courant de l'image
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
# Création de l'image rest-apis-flask-python :
# à partir du terminal, saisir (le . final pour répertoire courant de l'image)
# docker build -t flask-smorest-api .
# docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api
#
# Liste des containers :
# docker ps
#
# STOP container
# docker stop <container_id>
#
# REMOVE
# docker rm <container_id>
