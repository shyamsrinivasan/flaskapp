from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db


class User(db.Model):
    __tablename__ = 'test_users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    # def __init__(self, ids, name):
    #     self.id = ids
    #     self.name = name

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r})"
