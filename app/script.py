from flask import Flask, render_template
from app import app


@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')


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


@app.route('/login/index.html')
def login_home():
    return render_template('/login/index.html')


# @app.route()
def login_form():
    return render_template('/login/loginform.html')


# example forms using Flask and HTML
"""from flask import render_template, url_for, request, redirect
    app = Flask(__name__)
    
    
    @app.route('/')
    def index():
        return render_template('index.html')
        
    
    @app.route('/form', methods = ['GET', 'POST'])
    def form():
        if request.method == 'POST':
            glon = request.form['glon']
            return redirect(url_for('display.html', glon=glon))
            
        return render_template('form.html')
        
    
    @app.route('/return_form/<glon>')
    def return_form(glon):
        return render_template('return_form.html', glon=glon)"""


if __name__ == '__main__':
    app.run(debug=True)
