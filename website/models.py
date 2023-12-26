from website import db
# from flask_login import UserMixin
from sqlalchemy.sql import func


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    credit = db.Column(db.Float(3))
