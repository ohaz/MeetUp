from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


class Application:

    def __init__(self, config: Config):
        self.app: Flask = Flask(config.flask['name'])
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.create_db_uri(config)
        self.db: SQLAlchemy = SQLAlchemy(self.app)

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

    def create_db_uri(self, config: Config):
        dialect = config.sqlalchemy['dialect']
        driver = '+' + config.sqlalchemy['driver'] if config.sqlalchemy['driver'] != '' else ''
        username = config.sqlalchemy['username'] + ':' if config.sqlalchemy['username'] != '' else ''
        password = config.sqlalchemy['password'] + '@' if config.sqlalchemy['password'] != '' else ''
        host = config.sqlalchemy['host']
        port = ':' + config.sqlalchemy['port'] if config.sqlalchemy['port'] != '' else ''
        database = '/' + config.sqlalchemy['database'] if config.sqlalchemy['database'] != '' else ''
        engine_url = '{}{}://{}{}{}{}{}'.format(dialect, driver, username, password, host, port, database)
        return engine_url

application: Application = None
