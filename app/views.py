__author__ = 'pszemus'

from app import app
from flask import render_template, redirect, request, url_for
from forms import add_post, add_comment
from datebase import db, Post, Comment

blog_title = "Przemus"

@app.route('/')
@app.route('/index')
def index():
    date = Post.query.all()
    return render_template("index.html",
                           date=date,
                           title = "Przemus")


@app.route('/posts', defaults = {'foo': None})
@app.route('/posts/<foo>', methods=['GET', 'POST'])
def hello_login(foo = None):
    post_title = Post.query.filter_by(title=str(foo)).all()[0].title
    post_author = Post.query.filter_by(title=str(foo)).all()[0].author
    post = Post.query.filter_by(title=str(foo)).all()[0].post
    comments = Comment.query.filter_by(post_title=post_title)
    form = add_comment(request.form)

    if request.method == 'POST' and form.validate():
        print form.comment.data
        try5 = Comment(post_title, form.comment.data)
        db.session.add(try5)
        db.session.commit()
    return render_template("comment.html",
                           form=form,
                           post_title=post_title,
                           post_author=post_author,
                           comments=comments)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = add_post(request.form)
    if request.method == 'POST' and form.validate():
        print form.author.data, form.post.data, form.title.data, form
        try4 = Post(form.author.data, form.title.data, form.post.data)
        db.session.add(try4)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)
