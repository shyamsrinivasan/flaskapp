import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = os.urandom(32)


class TestConfig(Config):
    TESTING = True


config = {'development': DevConfig, 'testing': TestConfig, 'default': DevConfig}
