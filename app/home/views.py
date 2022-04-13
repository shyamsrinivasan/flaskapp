from flask import Blueprint, render_template, request
# from flask_bs4 import Bootstrap


home = Blueprint('home', __name__, template_folder='templates')


@home.route('/')
@home.route('/index.html')
def index():
    return render_template('/index.html')


@home.route('/login.html', methods=['GET', 'POST'])
def login_home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return render_template('/login_action_example.html', user=username)
    else:
        return render_template('/login.html')


@home.route('/signup.html')
def signup_home():
    return render_template('/signup.html')

