from flask import render_template, request
from app import app


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/index.html', methods=['GET', 'POST'])
def login_home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return render_template('/login/loginform.html', user=username)
    else:
        return render_template('/login/index.html')


@app.route('/admin/index.html')
def admin_home():
    return render_template('/admin/index.html')


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
