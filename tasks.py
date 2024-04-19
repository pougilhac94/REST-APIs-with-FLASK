import requests
import jinja2

from os import environ, path
from dotenv import load_dotenv

template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)

def render_template(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)

def send_simple_message(to, subject:str, body:str, html:str):
    """Service d'envoi de mails avec GunMail

    Args:
        to (mail): mail du destinataire
        subject (str): objet du mail
        body (str): texte du mail
        html (str): pour accepter du html

    Returns:
        service: envoi automatique du mail

    Note:
        Ne pas omettre d'importer current_app, pour récupérer les variables d'environnement chargées dans app.py
    """     
    # Specificy a `.env` file containing key/value config values
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))
    
    my_email_domain = environ.get("MAILGUN_DOMAIN")
    my_email_api_key = environ.get("MAILGUN_API_KEY")

    return requests.post(
		f"https://api.mailgun.net/v3/{my_email_domain}/messages",
		auth=("api", f"{my_email_api_key}"),
		data={"from": f"Boss Pougilhac <mailgun@{my_email_domain}>",
			"to": [to],
			"subject": subject,
			"text": body,
            "html": html,
            })

def send_user_registration_email(email, username:str):
    """Envoi d'un mail personnalisé suite à inscription

    Args:
        email (mail): mail du destinataire
        username (str): username

    Returns:
        service: envoi automatique du mail par appel de la fonction send_simple_message
    """
    # Specificy a `.env` file containing key/value config values
    return send_simple_message(
        email,
        "Inscription réussie",
        f"Bonjour {username}! Vous êtes maintenant inscrit sur Stores REST API.",
        render_template("email/action.html", username=username, render_url="https://rest-apis-with-flask.onrender.com/"),
    )