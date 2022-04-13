from flask import Flask
# from flask_bs4 import Bootstrap
# from .views.admin import admin
# from .views.taxes import taxes
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # configure application
    # app.config.from_mapping(SECRET_KEY='dev')
    app.config.from_object('config.TestConfig')
    # app.config['BOOTSTRAP_SERVE_LOCAL'] = True

    # Bootstrap(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        from .home import views
        # from .admin import views

        # registering blueprint with app
        app.register_blueprint(views.home_bp)
        # app.register_blueprint(admin)

    return app

    # from app import routes
