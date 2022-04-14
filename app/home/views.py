from flask import render_template, request, redirect, url_for
from . import home_bp
from .forms import ContactForm


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


@home_bp.route('/contact', methods=['GET', 'POST'])
def signup_home():
    form = ContactForm()
    if form.validate_on_submit():
        # process sign-up information using func into db
        return redirect(url_for("success"))
    else:
        # temporary render template to test usage of WTF-Forms
        return render_template('/contact.html')

