from flask import Blueprint, render_template
# from flask_bs4 import Bootstrap


home = Blueprint('home', __name__)


@home.route('/')
@home.route('/index.html')
def index():
    return render_template('/home/index.html')


@home.route('/login.html')
def admin_home():
    return render_template('/home/login.html')


@home.route('/signup.html')
def signup_home():
    return render_template('/home/signup.html')

