from flask import Blueprint, render_template
# from flask_bs4 import Bootstrap


home = Blueprint('home', __name__, template_folder='templates')


@home.route('/')
@home.route('/index.html')
def index():
    return render_template('/index.html')


@home.route('/login.html')
def admin_home():
    return render_template('/login.html')


@home.route('/signup.html')
def signup_home():
    return render_template('/signup.html')

