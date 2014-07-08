from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    post = db.Column(db.String(120), unique=True)
    author = db.Column(db.String(120), unique=True)



    def __init__(self, author, title, post):
        self.author = author
        self.title = title
        self.post = post
    '''
    def __repr__(self):
        return '<id: %r, author: %r, post: %r, title: %r>' % (self.id, self.author, self.post, self.title)
    '''

class comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String, ForeignKey("Post.post"))
    comment = db.Column(db.String(80), unique=True)

    def __init__(self, post_title, comment):
        self.post_title = post_title
        self.comment = comment