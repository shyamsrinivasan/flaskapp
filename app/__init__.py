from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import os


db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
flask_bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # configure application
    app.config.from_object('config.DevConfig')
    # app.config['SECRET_KEY'] =
    # app.config['BOOTSTRAP_SERVE_LOCAL'] = True

    csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'home.login_home'
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
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()

    return app

    # from app import routes
