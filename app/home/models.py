from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db
from app import flask_bcrypt


class User(db.Model):
    __tablename__ = 'test_users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30))
    phone = db.Column(db.String(10))
    username = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(60))

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, firstname={self.firstname!r}," \
               f"lastname={self.lastname!r}, email={self.email!r}, phone={self.phone!r}," \
               f"username={self.username!r})"
