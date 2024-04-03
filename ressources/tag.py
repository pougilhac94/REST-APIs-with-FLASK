from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TagModel, StoreModel, ItemModel
from schemas import TagSchema, TagAndItemSchema

blp = Blueprint("tags", __name__, description="Traitements sur les tags")

@blp.route("/store/<int:store_id>/tag")
class TagsInStore(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self, store_id):
        """Return all the tags of a store

        Args:
            store_id (int)

        Raises:
            404: Not found

        Returns:
            dict: store.tags

        """
        store = StoreModel.query.get_or_404(store_id)
        return store.tags.all()

    @blp.arguments(TagSchema)
    @blp.response(201, TagSchema)
    def post(self, tag_data, store_id):
        """Create a tag

        Args:
            tag (dict)
            store_id (int)

        Raises:
            404: store not found
            400: tag already exists
            500: SQLAlchemyError

        Returns:
            dict: tag

        """
        # exemple de contrôle de doublon, inutile ici car unicité imposée dans modele
        if TagModel.query.filter(
                                TagModel.store_id == store_id,
                                TagModel.name == tag_data["name"]
                                ).first():
            abort(400, message=str("Un tag de même nom existe déjà dans ce magasin"))
        else:
            tag = TagModel(**tag_data, store_id=store_id)
        
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as error:
            abort(500, message=str(error))
        else:
            return tag


@blp.route("/item/<int:item_id>/tag/<int:tag_id>")
class LinkTagsToItem(MethodView):
    @blp.response(201, TagSchema)
    def post(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        if item.store_id != tag.store_id:
            abort(500, message=f"Tag {tag_id} et objet {item_id} ne référencent pas le même magasin")
        else:
            item.tags.append(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message=f"Erreur lors de l'insertion du tag {tag_id} dans l'objet {item_id}")
        else:
            return tag

    @blp.response(200, TagAndItemSchema)
    def delete(self, item_id, tag_id):
        """Delete a link item-tag

        Args:
            item_id (int)
            tag_id (int)

        Raises:
            202: Erreur
            404: Tag ou Item inconnu

        Returns:
            message: tag_id and item_id 
        """
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.remove(tag)

        try:
            db.session.add(item)
            db.session.commit()      
        except SQLAlchemyError:
            abort(500, message="Erreur lors de la suppression du lien tag dans l'objet")
        else:
            return {"message": "L'objet n'est plus associé au tag", "item": item, "tag":tag}


@blp.route("/tag/<int:tag_id>")
class Tag(MethodView):
    @blp.response(200, TagSchema)
    def get(self, tag_id):
        """Return a tag

        Args:
            tag_id (int)

        Raises:
            404: Not found

        Returns:
            dict: tag
        """
        tag = TagModel.query.get_or_404(tag_id)
        return tag
    
    @blp.response(
        202, 
        description="Suppression d'un tag si aucun objet n'est associé",
        example={"message": "Tag supprimé"}
        )
    @blp.alt_response(404, description="Tag inconnu")
    @blp.alt_response(
        400, 
        description="Tag assigné à 1 ou plusieurs objets. Suppression impossible"
        )
    def delete(self, tag_id):
        """Delete a tag

        Args:
            tag_id (int)

        Raises:
            202: Tag supprimé
            400: Tag assigné à 1 ou plusieurs objets. Suppression impossible
            404: Tag inconnu

        Returns:
            message: tag_id 
        """
        tag = TagModel.query.get_or_404(tag_id)
        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return {"message": f"Tag {tag_id} supprimé"}
        else:
            abort(400, message=str("Suppression impossible, tag assigné à 1 ou plusieurs objets"))

 