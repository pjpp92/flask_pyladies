from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey

ROLE_USER = 0
ROLE_ADMIN = 1

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    post = db.Column(db.String(5000), unique=True)
    author = db.Column(db.String(50))


    def __init__(self, author, title, post):
        self.author = author
        self.title = title
        self.post = post


class Comment(db.Model):
    __tablename__ = 'Comment'
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String, ForeignKey('Post.id'))
    comment = db.Column(db.String(500))

    def __init__(self, post_title, comment):
        self.post_title = post_title
        self.comment = comment

