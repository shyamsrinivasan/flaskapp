from flask import render_template, request
from app import app
# from flask_bs4 import Bootstrap
#
#
# Bootstrap(app)


@app.route('/admin/client/index.html')
def client_home():
    return render_template('/admin/client/index.html')


@app.route('/office/index.html')
def office_home():
    return render_template('/admin/office/index.html')


@app.route('/taxes/index.html')
def taxes_home():
    return render_template('/taxes/index.html')


# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'username': 'User'}
#     posts = [
#         {'author': {'username': 'John'}, 'body': 'Beautiful day in New York'},
#         {'author': {'username': 'Smith'}, 'body': 'Cool comic book movie'}
#     ]
#     return render_template('index.html', title='Home', user=user, posts=posts)
    # '''
    # <html>
    #     <head>
    #         <title>Home Page - Microblog</title>
    #     </head>
    #     <body>
    #         <h1>Hello, ''' + user['username'] + '''!</h1>
    #     </body>
    # </html>'''
