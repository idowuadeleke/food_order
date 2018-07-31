import sqlite3
from db import db


class OrderItemModel(db.Model):
    __tablename__ = 'orderitems'

    id = db.Column(db.Integer, primary_key=True)
    quantity=db.Column(db.Integer)

    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    item= db.relationship('ItemModel')
    

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    

    def __init__(self,quantity,item_id,order_id):
        self.quantity=quantity
        self.order_id= order_id
        self.item_id=item_id

    def json(self):
        return {'order_item_id':self.id,'quantity': self.quantity,'order_id': self.order_id,'name':self.item.name,'price':self.item.price}


    @classmethod
    def find_by_order_id(cls,order_id):
        return cls.query.filter_by(order_id=order_id)

    @classmethod
    def find_by_orderitem_id(cls,orderitem_id):
        return cls.query.filter_by(id=orderitem_id)

    @classmethod
    def find_by_item_id(cls,item_id):
        return cls.query.filter_by(item_id=item_id)
        


  

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()