from configparser import ConfigParser, SectionProxy


class Config:

    def __init__(self, path: str):
        self.path: str = path
        self.config: ConfigParser = None
        self.flask: dict = dict()
        self.sqlalchemy: dict = dict()
        self.reload()

    def reload(self, path: str=None):
        if path is None:
            path = self.path
        self.config = ConfigParser()
        self.config.read(path)
        self.set_values()

    def set_values(self):

        # Flask
        self.flask = dict()
        flask_section: SectionProxy = self.config['Flask']
        self.flask['debug'] = flask_section.getboolean('debug', fallback=False)
        self.flask['ip'] = flask_section.get('ip', fallback='127.0.0.1')
        self.flask['port'] = flask_section.getint('port', fallback=7331)
        self.flask['name'] = flask_section.get('name', fallback='DefaultName')

        # SQLAlchemy
        self.sqlalchemy = dict()
        sqlalchemy_section: SectionProxy = self.config['SQLAlchemy']
        self.sqlalchemy['dialect'] = sqlalchemy_section.get('dialect', fallback='sqlite')
        self.sqlalchemy['driver'] = sqlalchemy_section.get('driver', fallback='')
        self.sqlalchemy['username'] = sqlalchemy_section.get('username', fallback='')
        self.sqlalchemy['password'] = sqlalchemy_section.get('password', fallback='')
        self.sqlalchemy['host'] = sqlalchemy_section.get('host', fallback='/meetup.db')
        self.sqlalchemy['port'] = sqlalchemy_section.get('port', fallback='')
        self.sqlalchemy['database'] = sqlalchemy_section.get('database', fallback='')
