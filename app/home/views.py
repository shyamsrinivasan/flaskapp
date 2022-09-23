from flask import render_template, request, redirect, url_for
from . import home_bp
from .forms import ContactForm, SignupForm, LoginForm
from .models import User
from app import db, flask_bcrypt
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


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
    # deal with a currently signed in user pressing login
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))

    form = LoginForm()
    # if request.method == 'POST':
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        check_user, user_obj = _check_user_password(username=username,
                                                    password=password)
        if check_user:
            # return 'Welcome {} {}'.format(user_obj.firstname, user_obj.lastname)
            login_user(user=user_obj)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('home.index')
            return redirect(next_page)
            # return render_template('/login_action_example.html',
            #                        firstname=user_obj.firstname,
            #                        lastname=user_obj.lastname,
            #                        user=username)
            # # redirect(url_for('home.success', from_page='login', firstname=firstname,
            # #                  lastname=lastname, username=username))
            # # return
        else:
            return 'Wrong username or password', 404
    else:
        return render_template('/login.html', form=form)


@home_bp.route('/logout')
def logout_home():
    """logout user"""
    logout_user()
    return redirect(url_for('home.index'))


@home_bp.route('/contact', methods=['GET', 'POST'])
@login_required
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
        _add_user(request.form)
        return redirect(url_for('home.success', from_page='signup'))
    #     flash('Addition of new user {} under progress'.format(form.username))
    return render_template('/signup.html', form=form)


def _add_user(form_obj):
    """take user details in form_obj to create User object and
    add as row to user table"""
    # generate user object
    new_user_obj = User(firstname=form_obj['first_name'], lastname=form_obj['last_name'],
                        email=form_obj['email'], phone=form_obj['phone'],
                        username=form_obj['username'])
    # add hashed password to db
    new_user_obj.set_password(form_obj['password'])
    db.session.add(new_user_obj)
    db.session.commit()
    return None


def _check_user_password(username, password):
    """check if password hash in db matches given username and password"""
    user_obj = db.session.query(User).filter(User.username == username).first()
    if user_obj is not None:
        if flask_bcrypt.check_password_hash(user_obj.password_hash, password.encode('utf-8')):
            return True, user_obj
        else:
            return False, None
    else:
        return False, None

