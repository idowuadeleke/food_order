import sqlite3
from flask_restful import Resource, reqparse
from models.order import OrderModel


class Order(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('status',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('quantity',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('total',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    
    #date

    def post(self):
        data = Order.parser.parse_args()

        order= OrderModel(**data)

        try:
            order.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return order.json(), 201

    def get(self, order_id):
        filtered_order = OrderModel.find_by_order_id(order_id).first()
        if filtered_order:
            return filtered_order.json()
        return {'message': 'Item not found'}, 404
        
            
class OrderByUserId(Resource):
    def get(self, user_id):
        filtered_order = OrderModel.find_by_user(user_id).first()
        if filtered_order:
            return filtered_order.json()
        return {'message': 'Item not found'}, 404

class OrderList(Resource):
    def get(self):
        return {'orders': list(map(lambda x: x.json(), OrderModel.query.all()))}
   

class OrderByItemId(Resource):
    def get(self, item_id):
        a=[]
        filtered_order = OrderModel.find_by_item_id(item_id)
        for item in filtered_order:
            order_id=item.order_id
            fil_order = OrderModel.find_by_order_id(order_id).first()
            a.append(fil_order.json())
        return a
        
