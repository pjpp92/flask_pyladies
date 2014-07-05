__author__ = 'pszemus'

from app import app
from flask import render_template, flash, redirect, request
import sqlite3
from datebase_try import try_it


conn = sqlite3.connect("datebase")
cursor = conn.cursor()

date = cursor.execute("SELECT * FROM post").fetchall()

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
        date=date)


@app.route('/form')
def my_form():
    return render_template("my-form.html")

@app.route('/form', methods=['POST', 'GET'])
def my_form_post():
    text = request.form['text']
    try_it(text)
    return render_template("my-form.html",
        text = text)