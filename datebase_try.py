import sqlite3

DATABASE = 'database'
conn = sqlite3.connect("datebase")
cursor = conn.cursor()


def add_table(name):
    cursor.execute("""create table %s(
    id integer primary key,
	author char(50) NOT NULL,
	post varcahr(5000) NOT NULL,
	title char(50) NOT NULL);""" %(name))

def add_record(author, post, title):
    cursor.execute("""INSERT INTO post(author, post, title)
                    VALUES('%s', '%s', '%s')""" %(author, post, title))
#add_table("post")
author = "Przemus"
post = 'Post1'
title = "Try1"
#add_record(author, post, title)

results = cursor.execute("SELECT * FROM post")
print results

conn.commit()