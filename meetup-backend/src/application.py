from flask import Flask
from config import Config


class Application:

    def __init__(self, config: Config):
        self.app: Flask = Flask(config.flask['name'])

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)


application: Application = None
