import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.user import UserRegister,UserList,UserById
from resources.item import Item, ItemList
from resources.order import Order,OrderByUserId,OrderList,OrderByItemId
from resources.order_item import OrderItem


app = Flask(__name__)


app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


api.add_resource(UserList, '/api/users')
api.add_resource(UserById, '/api/users/<int:id>')
api.add_resource(Item, '/api/items/<int:_id>')
api.add_resource(ItemList, '/api/items')
api.add_resource(Order, '/api/orders/<int:order_id>')
api.add_resource(OrderItem, '/api/orderitem/<int:orderitem_id>')
api.add_resource(OrderByUserId, '/api/users/<int:user_id>/orders')
api.add_resource(OrderList, '/api/orders')
api.add_resource(OrderByItemId, '/api/items/<int:item_id>/orders')

api.add_resource(UserRegister, '/register')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)



