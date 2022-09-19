from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db


class User(db.Model):
    __tablename__ = 'test_users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30))
    phone = db.Column(db.String(10))
    username = db.Column(db.String(6), nullable=False)

    # def __init__(self, ids, name):
    #     self.id = ids
    #     self.name = name

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r})"
