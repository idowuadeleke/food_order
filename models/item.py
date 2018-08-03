import sqlite3
from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    quantity= db.Column(db.Integer)


    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity=quantity

    def json(self):
        return {'id':self.id,'name': self.name, 'price': self.price, 'quantity':self.quantity}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()