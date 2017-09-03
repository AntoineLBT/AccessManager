from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel',
            'name': 'Despacito'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'nickname': 'Antoine'},
            'body': 'Nique ta mere!'
        }
    ]
    return render_template('index.html',title='Home',user = user, posts=posts)
