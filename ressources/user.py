from flask_smorest import Blueprint, abort
from flask.views import MethodView
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt
import requests
import re

from db import db
from blocklist import BLOCKLIST
from models import UserModel
from schemas import UserSchema, UserRegisterSchema
from flask import current_app

blp = Blueprint("users", __name__, description="Traitements sur les utilisateurs")

def send_simple_message(to, subject, body):
    """Service d'envoi de mails avec GunMail

    Returns:
        request POST: envoi du mail
    
    Note:
        Ne pas omettre d'importer app, pour récupérer les variables d'environnement chargées dans app.py
    """
    my_domain = current_app.config.get("EMAIL_DOMAIN")
    my_key = current_app.config.get("EMAIL_API_KEY")

    return requests.post(
		f"https://api.mailgun.net/v3/{my_domain}/messages",
		auth=("api", f"{my_key}"),
		data={"from": f"Boss Pougilhac <mailgun@{my_domain}>",
			"to": [to],
			"subject": subject,
			"text": body})
 
def check(email):
    """Validation d'un email par expression régulière

    Args:
        email : nom@service.extension

    Returns:
        raise error or None
    """
    # pass the regular expression
    # and the string into the fullmatch() method
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

@blp.route("/user/<int:user_id>")
class User(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": f"Utilisateur {user_id} supprimé"}, 200


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserRegisterSchema)
    @blp.response(201, UserRegisterSchema)
    def post(self, user_data):
        if  not check(user_data["email"]):
            abort(409, message="Email invalide")

        user = UserModel(
            username = user_data["username"],
            password = pbkdf2_sha256.hash(user_data["password"]),
            email = user_data["email"]
        )

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(409, message="Un utilisateur avec ce nom ou ce mail existe déjà")
        except SQLAlchemyError:
            abort(500, message="Erreur lors de l'insertion de l'utillisateur dans la table")
        else:
            send_simple_message(user_data["email"], 'Inscription', 'Bienvenue !')
            return {"message": "Identifiant créé, vous avez reçu un mail de confirmation"}, 201


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}
        else:
            abort(401, message=f"Identifiant {user_data['username']} invalide")


@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        # Make it clear that when to add the refresh token to the blocklist will depend on the app design
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"access_token": new_token, "identity": current_user}, 200


@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt().get("jti")
        BLOCKLIST.add(jti)
        return {"message": "Utilisateur déconnecté"}, 200


@blp.route("/users_list")    
class UserList(MethodView):
    @jwt_required()
    def get(self):
        return UserModel.query.all()