from app import app
from flask import render_template, current_app, abort, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', page_name='index')


@app.route('/about')
def about():
    return render_template('about.html', page_name='about')


@app.route('/shutdown')
def server_shutdown():
    if not current_app.testing:
        abort(404)
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if not shutdown:
        abort(500)
    shutdown()
    return 'Shutting down...'
