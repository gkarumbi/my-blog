from flask import Flask, render_template
from app import app
from datetime import datetime

@app.route('/index')
def index():
    return render_template('index.html',message=message)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html',
    current_time=datetime.utcnow())