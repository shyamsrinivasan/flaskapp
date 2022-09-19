from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

import os


db = SQLAlchemy()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # configure application
    app.config.from_object('config.DevConfig')
    # app.config['SECRET_KEY'] =
    # app.config['BOOTSTRAP_SERVE_LOCAL'] = True

    csrf.init_app(app)
    # Bootstrap(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .home import home_bp
    from .admin import admin_bp
    from .taxes import taxes_bp

    # registering blueprint with app
    app.register_blueprint(home_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(taxes_bp)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

    # from app import routes
