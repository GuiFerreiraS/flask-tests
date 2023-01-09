import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema


blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route('/store')
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return list(stores.values())

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store, 201


@blp.route('/store/<string:store_id>')
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id], 201
        except KeyError:
            abort(404, message="Store not found.")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted successfully"}
        except KeyError:
            abort(404, message="Store not found.")
