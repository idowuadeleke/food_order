import sqlite3
from db import db
from order_item import OrderItemModel


class OrderModel(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    date=db.Column(db.Date)
    status=db.Column(db.Integer)
    total=db.Column(db.Float(precision=2))
    quantity=db.Column(db.Integer)
    #date=db.Column(db.date)
    user_name= db.Column(db.Integer, db.ForeignKey('users.username'))
   
    order_items=db.relationship('OrderItemModel')
    
    

    
    

    def __init__(self,date,quantity,status,total,user_name):
        self.quantity= quantity
        self.status = status
        self.total = total
        self.user_name= user_name


    def json(self):
        order_item=OrderItemModel.find_by_order_id(self.id).all()
        return {'id':self.id,'status': self.status,'total': self.total,
        'username':self.user_name,'items':[item.json() for item in order_item]}

    @classmethod
    def find_by_user(cls, user_name):
        return cls.query.filter_by(user_name=user_name)

    @classmethod
    def find_by_order_id(cls,_id):
        return cls.query.filter_by(id=_id)

    @classmethod
    def find_by_item_id(cls,item_id):
        orders_id_by_item=OrderItemModel.find_by_item_id(item_id).all()
        return orders_id_by_item

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()