from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Coloumn(db.String(100), unique=True)
    password = db.Coloumn(db.String(150))
    first_name = db.Coloumn(db.String(150))