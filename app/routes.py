from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tyberius'}
    posts = [
        {
            'author': {'username': 'Dax'},
            'body': 'Loaded VA-07 data'
        },
        {
            'author': {'username': 'Picard'},
            'body': 'Approved VA-07 data'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
