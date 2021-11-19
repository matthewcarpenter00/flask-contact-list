from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# here is the actual database structure
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    # represenation method
    # this will return a string %r is equal to what is after % - you can do multiple by adding more %r - google syntax
    # this is mostly for us when we access a record just to see what record we are accessing
    # in the terminal it will show as <User matthew@gmail.com>
    # def __repr__(self):
    #     return '<User %r>' % self.email

    # serialize to convert the code to be readable and send them to the front end
    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "email": self.email,
            # do not serialize the password, its a security breach
        # }

# this file will change the database
# it has more impact than anything else 
# we cant have incomplete records, we cant have overlapping records

# whenever we make changes here  to the database you have to run the following commands:
# - $ pipenv run migrate create database migrations (if models.py is edited)
# - $ pipenv run upgrade run database migrations (if pending)
# - $ pipenv run start start flask web server (if not running)
# - $ pipenv run deploy deploy to heroku (if needed) 


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.full_name

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address
        }