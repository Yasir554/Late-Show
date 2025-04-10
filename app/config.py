import os

class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "../instances/lateShowDb.sqlite3")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False