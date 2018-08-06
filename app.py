import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.user import UserRegister,UserList,UserByName
from resources.item import Item, ItemList
from resources.order import Order,OrderByUserName,OrderList,OrderByItemName
from resources.order_item import OrderItem


app = Flask(__name__)


app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


api.add_resource(UserList, '/api/users')
api.add_resource(UserByName, '/api/users/<string:username>')
api.add_resource(Item, '/api/items/<string:name>') 
api.add_resource(ItemList, '/api/items')
api.add_resource(Order, '/api/orders/<int:ref>')
api.add_resource(OrderItem, '/api/orderitem/<int:orderitem_id>') 
api.add_resource(OrderByUserName, '/api/users/<string:user_name>/orders')
api.add_resource(OrderList, '/api/orders')
api.add_resource(OrderByItemName, '/api/items/<string:name>/orders')

api.add_resource(UserRegister, '/register')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    

