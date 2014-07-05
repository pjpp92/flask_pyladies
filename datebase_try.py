import sqlite3
import datetime


conn = sqlite3.connect("datebase")
cursor = conn.cursor()

new= str(datetime.datetime.now())[:-7]
print new

def add_table(name):
    cursor.execute("""create table %s(id integer primary key,
	author char(50) NOT NULL,
	post varcahr(50000) NOT NULL,
	title char(50) NOT NULL,
	date_created datetime NOT NULL);""" %(name))

def add_record(author, post, title, date):
    cursor.execute("INSERT INTO post(author, post, title, date_created) "
                   "VALUES(%s, %s, %s, %s)" %(author, title, post, date))

def try_it(example):
    print example

results = cursor.execute("SELECT * FROM post").fetchall()

conn.commit()