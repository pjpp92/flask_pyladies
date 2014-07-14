__author__ = 'pszemus'

from app import app
from flask import render_template, redirect, request, url_for, session, flash
from forms import add_post, add_comment
from datebase import db, Post, Comment
from functools import wraps

blog_title = "Przemus"

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You have to login first')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@app.route('/index')
def index():
    date = Post.query.all()
    return render_template("index.html",
                           date=date,
                           blog_title = blog_title)


@app.route('/posts', defaults = {'foo': None})
@app.route('/posts/<foo>', methods=['GET', 'POST'])
def comment(foo = None):
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
                           blog_title = blog_title,
                           post_title=post_title,
                           post_author=post_author,
                           post = post,
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

@app.route('/admin')
@login_required
def admin():
    date = Post.query.all()
    return render_template('admin.html', date=date,
                           blog_title=blog_title)


@app.route('/admin/posts', defaults = {'foo': None})
@app.route('/admin/posts/<foo>', methods=['GET', 'POST'])
@login_required
def edit_post(foo):
    post = Post.query.filter_by(title=str(foo)).all()[0]
    comments = Comment.query.filter_by(post_title=post.title)
    if request.method == 'POST':
        if request.form.get('delete_post', None) == "delete":

            bar = Post.query.filter_by(title=str(foo)).first()
            piwo = Comment.query.filter_by(post_title=str(foo))
            for item in piwo:
                db.session.delete(item)
            db.session.delete(bar)
            db.session.commit()
            return redirect(url_for('admin'))

        else:
            for item in comments:
                if request.form.get(item.comment, None) == "delete":
                    db.session.delete(item)
                    db.session.commit()
    return render_template('admin_post.html', post=post, comments=comments,
                           blog_title=blog_title)

@app.route('/logout')
def logout():
    flash("You're logout")
    session.pop('logged_in', None)
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid user name or password'
        else:
            session['logged_in'] = True
            return redirect(url_for('admin'))
    return render_template('login.html', error=error,
                           blog_title=blog_title)

