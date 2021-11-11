
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), nullable = False, unique = True)
    email = db.Column(db.String(32), nullable = False, unique = True)
    password = db.Column(db.String(32), nullable = False)
    apiKey = db.Column(db.String(200), nullable = False, unique = True)

    def __init__(self,usr, email, passw, k):
        self.username = usr
        self.email = email
        self.password = passw
        self.apiKey = k

    def __repr__(self):
        return f'User({self.id},{self.username}, {self.email}, {self.password}, {self.apiKey})'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    author = db.Column(db.String(32))
    genre = db.Column(db.String(32))

    def __init__(self,u, e, p):
        self.name= u
        self.author = e
        self.genre = p

    def object_as_dict(obj):
        li =[]
        for one in obj:
            li.append({c.key: getattr(one, c.key)
                    for c in inspect(one).mapper.column_attrs}) 
        return li

    # def __repr__(self):
    #     return f'User({self.id},{self.name}, {self.author}, {self.genre})'
