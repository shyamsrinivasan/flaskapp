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


if __name__ == '__main__':
    app.run(debug=True)
