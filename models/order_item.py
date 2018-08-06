import sqlite3
from db import db


class OrderItemModel(db.Model):
    __tablename__ = 'orderitems'

    id = db.Column(db.Integer, primary_key=True)
    quantity=db.Column(db.Integer)

    item_name = db.Column(db.String, db.ForeignKey('items.name'))
    item= db.relationship('ItemModel')
    

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    

    def __init__(self,quantity,item_name,order_id):
        self.quantity=quantity
        self.order_id= order_id
        self.item_name=item_name


    def json(self):
        return {'id':self.item.id,'name':self.item_name,'price':self.item.price} #

    
    #def item_quantity_check(self):
        #if self.item.quantity==0:
            #return 1
        #elif self.item.quantity < self.quantity:
            #return 2
        #elif self.item.quantity >= self.quantity:
            #self.item.quantity=self.item.quantity - self.quantity
            #return 3

    @classmethod
    def find_by_order_id(cls,order_id):
        return cls.query.filter_by(order_id=order_id)

    @classmethod
    def find_by_orderitem_id(cls,orderitem_id):
        return cls.query.filter_by(id=orderitem_id)

    @classmethod
    def find_by_item_id(cls,item_id):
        return cls.query.filter_by(item_id=item_id)
        
    @classmethod
    def find_by_item_name(cls,name):
        return cls.query.filter_by(item_name=name)
        

  

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()