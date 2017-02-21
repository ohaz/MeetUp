import os
from config import Config
import sys
import shutil
from application import application, Application
import application
import time


def main():
    config = Config(sys.argv[1])
    application.application = Application(config)
    dialect = config.sqlalchemy['dialect']
    driver = '+' + config.sqlalchemy['driver'] if config.sqlalchemy['driver'] != '' else ''
    username = config.sqlalchemy['username'] + ':' if config.sqlalchemy['username'] != '' else ''
    password = config.sqlalchemy['password'] + '@' if config.sqlalchemy['password'] != '' else ''
    host = config.sqlalchemy['host']
    port = ':' + config.sqlalchemy['port'] if config.sqlalchemy['port'] != '' else ''
    database = '/' + config.sqlalchemy['database'] if config.sqlalchemy['database'] != '' else ''
    engine_url = '{}{}://{}{}{}{}{}'.format(dialect, driver, username, password, host, port, database)
    application.application.app.config['SQLALCHEMY_DATABASE_URI'] = engine_url
    if config.sqlalchemy['dialect'] == 'sqlite':
        if os.path.exists('.'+host):
            shutil.move('.'+host, '.'+host+'.backup'+str(int(time.time())))
        from models.group import Group
        from models.user import User
        db = application.application.db
        g = Group('TEST')
        u = User()
        db.session.add(g)
        db.session.add(u)
        g.users.append(u)
        db.create_all()
        db.session.commit()
    else:
        print('No set up found for dialect', config.sqlalchemy['dialect'])


if __name__ == '__main__':
    if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
        print('config file required')
        exit(-1)
    main()
