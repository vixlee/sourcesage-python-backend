from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String(120))
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    image = db.Column(db.String)

    def __init__(self, email, password, name, age, gender, image = None):
        self.email = email
        self.password = password
        self.name = name
        self.age = age
        self.gender = gender
        self.image = image

class UserSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    gender = fields.Integer(required=True)
    image = fields.String()
    class Meta:
        fields = ('email', 'password', 'name', 'age', 'gender','image')

class LoginFormSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
    class Meta:
        fields = ('email', 'password',)

class ResetPasswordSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
    confirm = fields.String(required=True)
    class Meta:
        fields = ('email', 'password', 'confirm',)

user_schema = UserSchema()
login_form_schema = LoginFormSchema()
reset_password_schema = ResetPasswordSchema()
