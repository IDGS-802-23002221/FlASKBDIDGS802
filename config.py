

class Config(object):
    SECRET_KEY='Clave nueva'
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456789@127.0.0.1/idgs802'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
