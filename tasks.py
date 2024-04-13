import requests

from os import environ, path
from dotenv import load_dotenv
# Specificy a `.env` file containing key/value config values
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

def send_simple_message(to, subject:str, body:str):
    """Service d'envoi de mails avec GunMail

    Args:
        to (mail): mail du destinataire
        subject (str): objet du mail
        body (str): texte du mail

    Returns:
        service: envoi automatique du mail

    Note:
        Ne pas omettre d'importer current_app, pour récupérer les variables d'environnement chargées dans app.py
    """
     
    my_email_domain = environ.get("EMAIL_DOMAIN")
    my_email_api_key = environ.get("EMAIL_API_KEY")

    return requests.post(
		f"https://api.mailgun.net/v3/{my_email_domain}/messages",
		auth=("api", f"{my_email_api_key}"),
		data={"from": f"Boss Pougilhac <mailgun@{my_email_domain}>",
			"to": [to],
			"subject": subject,
			"text": body})

def send_user_registration_email(email, username:str):
    """Envoi d'un mail personnalisé suite à inscription

    Args:
        email (mail): mail du destinataire
        username (str): username

    Returns:
        service: envoi automatique du mail par appel de la fonction send_simple_message
    """
    return send_simple_message(
        email,
        "Inscription réussie",
        f"Bonjour {username}! Vous êtes maintenant inscrit sur Stores REST API.",
    )