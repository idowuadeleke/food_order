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

    def get(self, ref):
        filtered_order = OrderModel.find_by_reference(ref).first()
        if filtered_order:
            return filtered_order.json()
        return {'message': 'Item not found'}, 404
        
            
class OrderByUserName(Resource):
    def get(self, user_name):
        filtered_order = OrderModel.find_by_user(user_name)
        a=[]
        if filtered_order:
            for order in filtered_order:
                a.append(order.json())
        return a
    

class OrderList(Resource):
    def get(self):
        return  list(map(lambda x: x.json(), OrderModel.query.all()))
   

class OrderByItemName(Resource):
    def get(self,name):
        a=[]
        filtered_order = OrderModel.find_by_item_name(name)
        for item in filtered_order:
            order_id=item.order_id
            fil_order = OrderModel.find_by_order_id(order_id).first()
            a.append(fil_order.json())
        return a
        
