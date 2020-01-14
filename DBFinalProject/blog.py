#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 11:17:57 2018

@author: shanekelley
"""

import os
import sqlite3
from flask import Flask, request, render_template, g

# Create the application
app = Flask(__name__)

#####################################################
# Database handling 
  
def connect_db():
    """Connects to the database."""
    debug("Connecting to DB.")
    conn = sqlite3.connect(os.path.join(app.root_path, 'blog.db'))
    conn.row_factory = sqlite3.Row
    return conn
    
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
    
@app.teardown_appcontext
def close_db(error):
    """Closes the database automatically when the application
    context ends."""
    debug("Disconnecting from DB.")
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

######################################################
# Command line utilities 
        
def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def init_db_command():
    """Initializes the database."""
    print("Initializing DB.")
    init_db()
    
    
#####################################################
# Debugging

def debug(s):
    """Prints a message to the screen (not web browser) 
    if FLASK_DEBUG is set."""
    if app.config['DEBUG']:
        print(s)
        
        
#####################################################
def populate_db():
    db=get_db()
    with app.open_resource('populate.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    
    
@app.cli.command('populatedb')
def populate_db_command():
    """Populates the databalse."""
    print("Populating DB.")
    populate_db()
    
    
    
    
    
    
#######################################################
@app.route("/")
def homepage():
    return render_template('home.html')
    
    
    
    
    
    
    
    
    
@app.route("/dump")
def dump_entries():
    db = get_db()
    rows = db.execute('select id, date, title, content from entries order by date')
    output = ""
    for r in rows:
        debug(str(dict(r)))
        output += str(dict(r))
        output += "\n"
    return "<pre>" + output + "</pre>"



@app.route("/browse")
def browse():
    db = get_db()
    rows = db.execute('select id, date, title, content from entries order by date')
    rowlist = rows.fetchall()
    return render_template('browse.html', entries=rowlist)



@app.route("/write", methods=['get', 'post'])
def write():
    # Step 1, display form
    if "step" not in request.form:     
        return render_template('write.html', step="compose_entry")
    
    # Step 2, add blog post to database.
    elif request.form["step"] == "add_entry":
        db = get_db()
        db.execute("insert into entries (date, title, content) values (datetime('now', 'localtime'), ?, ?)",
                   [request.form['title'], request.form['content']])
        db.commit()
        return render_template("write.html", step="add_entry")