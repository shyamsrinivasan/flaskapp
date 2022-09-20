from flask import render_template, request, redirect, url_for
from . import home_bp
from .forms import ContactForm, SignupForm, LoginForm
from .models import User
from app import db
from app import flask_bcrypt


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
    form = LoginForm()
    # if request.method == 'POST':
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        # query db and get user and corresponding pass word hash
        user_obj = db.session.query(User).filter(User.username == username).first()
        if user_obj is not None and \
                flask_bcrypt.check_password_hash(user_obj.password_hash, password):
            return 'Welcome {} {}'.format(user_obj.firstname, user_obj.lastname)
        else:
            return 'User not found', 404
        # u = User(name=username)
        # db.session.add(u)
        # db.session.commit()
        # return render_template('/login_action_example.html', user=username)
    else:
        return render_template('/login.html', form=form)


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
    # if request.method == 'POST':
        # return 'Signup Successful!'
    # print(form['csrf_token'])
    if form.validate_on_submit():
        # process sign-up information using func into db add info to db here
        add_user(request.form)
        return redirect(url_for('home.success', from_page='signup'))
    #     flash('Addition of new user {} under progress'.format(form.username))
    return render_template('/signup.html', form=form)


def add_user(form_obj):

    # hash password using bcrypt
    hashed = flask_bcrypt.generate_password_hash(password=form_obj['password'], rounds=12)
    # generate user object to add to db with hashed password
    new_user_obj = User(firstname=form_obj['first_name'], lastname=form_obj['last_name'],
                        email=form_obj['email'], phone=form_obj['phone'],
                        username=form_obj['username'], password_hash=hashed)
    db.session.add(new_user_obj)
    db.session.commit()
    return None


