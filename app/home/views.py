from flask import render_template, request, redirect, url_for
from . import home_bp
from .forms import ContactForm, SignupForm
from .models import User
from app import db


@home_bp.route('/')
@home_bp.route('/index')
def index():
    """home page"""
    return render_template('/index.html')


@home_bp.route('/faq')
def faq():
    """FAQs page"""
    return render_template('/faq.html')


@home_bp.route('/about')
def about():
    """about page"""
    return render_template('/about.html')


@home_bp.route('/login', methods=['GET', 'POST'])
def login_home():
    """login page"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        u = User(name=username)
        db.session.add(u)
        db.session.commit()
        return render_template('/login_action_example.html', user=username)
    else:
        return render_template('/login.html')


@home_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """contact us page"""
    form = ContactForm()
    # print(form.validate_on_submit())
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('home.success', from_page='contact'))
        # if form.validate_on_submit():
        #     name = form.name.data
        #     mail_id = form.email.data
        #     return 'Message for {} sent with contact {} with value: {}'.format(name, mail_id, form.validate_on_submit())
        # else:
        #     if form.name.errors:
        #         # x = form.name.errors[0]
        #         # for err in form.name.errors:
        #         #     x += err.jo
        #         return 'Form name error'
        #     elif form.email.errors:
        #         return 'Form email error'
        #     elif form.message.errors:
        #         return 'Form message error'
        #     elif form.errors:
        #         return render_template('/fail.html', form=form)
        #         # return 'Form has errors'
        #     else:
        #         return 'Unknown error'
        #     return render_template('/fail.html', form=form)
    return render_template('/contact.html', form=form)


@home_bp.route('/<from_page>/success')
def success(from_page):
    """success page views/routes for different sections of app"""
    return render_template('/success.html', page=from_page)
    # if from_page == 'contact':
    #     return render_template('/success.html')
    # elif from_page == 'signup':
    #     return render_template('/success.html')
    # return redirect(url_for('home.index'))
    # return render_template('/success.html')


@home_bp.route('/signup', methods=['GET', 'POST'])
def signup_home():
    form = SignupForm()
    if request.method == 'POST':
        # add info to db here
        return 'Signup Successful!'
        # return redirect(url_for('home.index.html')
    # if form.validate_on_submit():
        # process sign-up information using func into db
        # return redirect(url_for('success', from_page='signup'))
    # temporary render template to test usage of WTF-Forms
    return render_template('/signup.html', form=form)

