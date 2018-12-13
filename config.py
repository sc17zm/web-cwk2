import os

basedir = os.path.abspath(os.path.dirname(__file__))

#implementing sqlalchemy to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

#security of the pages
WTF_CSRF_ENABLED = True
SECRET_KEY = 'user-book-read'
