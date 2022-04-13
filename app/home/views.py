from flask import render_template, request
from . import home_bp


@home_bp.route('/')
@home_bp.route('/index')
def index():
    return render_template('/index.html')


@home_bp.route('/about')
def about():
    return render_template('/about.html')


@home_bp.route('/login', methods=['GET', 'POST'])
def login_home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return render_template('/login_action_example.html', user=username)
    else:
        return render_template('/login.html')


@home_bp.route('/signup', methods=['GET', 'POST'])
def signup_home():
    if request.method == 'POST':
        # process sign-up information using func into db
        return None
    else:
        # temporary render template to test usage of WTF-Forms
        return render_template('/contact.html')

