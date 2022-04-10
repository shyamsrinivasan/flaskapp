from flask import Flask, render_template, url_for, request, redirect


# example forms using Flask and HTML
app = Flask(__name__)


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


# @app.route('/login/display_login', methods=['GET', 'POST'])
# def display_login():
#     if request.method == 'POST':
#         username = request.form['username']
#         return render_template('/login/loginform.html', user=username)
#
#     return render_template('/login/index.html')


# @app.route('/return_form/<glon>')
# def return_form(glon):
#     return render_template('return_form.html', glon=glon)


if __name__ == '__main__':
    app.run(debug=True)