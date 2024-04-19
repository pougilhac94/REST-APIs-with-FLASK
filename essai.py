from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
print(f'{basedir=}')
load_dotenv(path.join(basedir, ".env"))
essai_my_email_domain = environ.get("MAILGUN_DOMAIN")
print(f'{essai_my_email_domain=}')
essai_uri = environ.get('DEV_DATABASE_URL', 'sqlite:///sqlite_stores.db')
print(f'{essai_uri=}')