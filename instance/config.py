import os

basedir = os.path.abspath(os.path.dirname(__file__))
basedir_split = basedir.split("/")
basedir = '/'.join([i for i in basedir_split[0:-1]]) + "/"


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_sqlite')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    IMAGES_FOLDER = os.path.join(basedir, 'images_icons')
    UPLOAD_FOLDER = '/files/'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    ALLOWED_EXTENSIONS = {'txt', 'csv'}


class ProductionConfig(Config):
    DEBUG = False


class DevelopConfig(Config):
    DEBUG = True
    #ASSETS_DEBUG = True