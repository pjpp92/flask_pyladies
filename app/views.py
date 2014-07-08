__author__ = 'pszemus'

from app import app
from flask import render_template, redirect, request, url_for
from forms import add_post
from datebase import db, Post


@app.route('/')
@app.route('/index')
def index():
    date = Post.query.all()
    return render_template("index.html",
                           date=date,
                           title = "Przemus")

@app.route('/posts', defaults = {'foo': None})
@app.route('/posts/<foo>')
def hello_login(foo = None):
    x=Post.query.filter_by(id=int(foo))
    return x.all()[0].title


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