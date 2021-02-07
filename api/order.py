# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

# project resources
from models.orders import Orders


class OrdersApi(Resource):
    """
    Flask-resftul resource for returning db.order collection.

    :Example:

    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config

    # Create flask app, config, and resftul api, then add OrdersApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(OrdersApi, '/order/')

    """
    @jwt_required
    def get(self) -> Response:
        """
        GET response method for all documents in order collection.
        JSON Web Token is required.

        :return: JSON object
        """
        output = Orders.objects()
        return jsonify({'result': output})

    @jwt_required
    def post(self) -> Response:
        """
        POST response method for creating order.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)

        :return: JSON object
        """
        data = request.get_json()
        post_order = Orders(**data).save()
        output = {'id': str(post_order.id)}
        return jsonify({'result': output})


class OrderApi(Resource):
    """
    Flask-resftul resource for returning db.order collection.

    :Example:

    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config

    # Create flask app, config, and resftul api, then add OrderApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(OrderApi, '/order/<order_id>')

    """
    @jwt_required
    def get(self, order_id: str) -> Response:
        """
        GET response method for single documents in order collection.

        :return: JSON object
        """
        output = Orders.objects.get(id=order_id)
        return jsonify({'result': output})

    @jwt_required
    def put(self, order_id: str) -> Response:
        """
        PUT response method for updating a order.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)

        :return: JSON object
        """
        data = request.get_json()
        put_order = Orders.objects(id=order_id).update(**data)
        return jsonify({'result': put_order})

    @jwt_required
    def delete(self, order_id: str) -> Response:
        """
        DELETE response method for deleting single order.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)

        :return: JSON object
        """
        output = Orders.objects(id=order_id).delete()
        return jsonify({'result': output})