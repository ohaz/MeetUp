from config import Config
from application import Application
import application


def main():
    config = Config('config.ini')
    application.application = Application(config)
    import views
    application.application.run(host=config.flask['ip'], port=config.flask['port'], debug=config.flask['debug'])

if __name__ == '__main__':
    main()
