import sqlite3
from flask_restful import Resource, reqparse
from models.order_item import OrderItemModel


class OrderItem(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('quantity',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('order_id',
                        type=int,
                        required=True,
                        help="Every item orderd needs an order id."
                        )
    parser.add_argument('item_id',
                        type=int,
                        required=True,
                        help="Every item orderd needs an order id."
                        )

    def post(self):
        data = OrderItem.parser.parse_args()

        orderitem = OrderItemModel(**data)

        try:
            orderitem.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return orderitem.json(), 201

    def get(self, orderitem_id):
        myitem = OrderItemModel.find_by_orderitem_id(orderitem_id).first()
        if myitem:
            return myitem.json()
        return {'message': 'Item not found'}, 404