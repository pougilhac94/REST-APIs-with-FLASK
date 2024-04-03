from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Traitements sur les articles")

@blp.route("/item/<int:item_id>")
class Item(MethodView):
    """Ensemble des traitements de la classe Item
    
    Args:
        method: MethodView
    
    URL :
        /item/<item_id>    
    """
    @jwt_required()
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        """Retourne l'item demandé
        
        Args:
            item_id (int): index

        Raises:   
            404: Not found

        Returns:
            dict: item
        """
        item = ItemModel.query.get_or_404(item_id)
        return item
    
    @jwt_required()
    @blp.response(200, ItemSchema)
    def delete(self, item_id):
        """Supprime l'item demandé

        Args:
            item_id (int): index
        
        Raises:   
            404: Not found

        Returns:
            message: item_id
        """
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": f"Article {item_id} supprimé"}
    
    @jwt_required()
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        """Mise à jour ou création de l'item demandé

        Args:
            item (dict)
            item_id (int): index
        
        Raises:   
            404: Not found

        Returns:
            dict: item
        """
        item = ItemModel.query.get_or_404(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)
        
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/item")
class ItemList(MethodView):
    """Ensemble des traitements de la classe ItemList
    """
    @jwt_required()
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        """Retourne la liste détaillée de tous les objets
        
        Raises:   
            200: OK

        Returns:
            list: dictionnaire item
        """
        return ItemModel.query.all()
    
    @jwt_required(fresh=True)
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        """Ajoute un item

        Args:
            dict: description de l'item

        Raises:   
            500: SQLAlchemyError
        
        Returns:
            dict: item ajouté
        """
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Erreur lors de l'insertion de l'article dans la table")
        else:
            return item