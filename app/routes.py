from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'User'}
    posts = [
        {'author': {'username': 'John'}, 'body': 'Beautiful day in New York'},
        {'author': {'username': 'Smith'}, 'body': 'Cool comic book movie'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    # '''
    # <html>
    #     <head>
    #         <title>Home Page - Microblog</title>
    #     </head>
    #     <body>
    #         <h1>Hello, ''' + user['username'] + '''!</h1>
    #     </body>
    # </html>'''
