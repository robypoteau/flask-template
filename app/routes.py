from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', page_name = 'index')

@app.route('/about')
def about():
    return render_template('about.html', page_name = 'about')
