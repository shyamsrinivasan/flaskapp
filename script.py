from flask import Flask


# flask contructor takes current module name an input arg
app = Flask(__name__)
# Flask.route() is a decorator. Tells which URL should call associated function
# @app.route('/')
@app.route('/<name>')
# / is the URL bound to hello_world()
# def hello_world():
#     return 'Hello World'
def hello_name(name):
    return 'Hello %s' %name


if __name__ == '__main__':
    # Flask.run() runs application on local server
    app.run()
