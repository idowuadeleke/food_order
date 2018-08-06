import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer)
    username = db.Column(db.String(80), primary_key=True)
    name=db.Column(db.String(100))

    def __init__(self,name,username):
        self.name=name
        self.username = username

    def json(self):
        return {'id': self.id, 'name': self.name,'username': self.username}
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, user_name):
        return cls.query.filter_by(username=user_name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


