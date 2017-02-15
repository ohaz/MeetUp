from application import application


@application.app.route('/')
def index():
    return 'HELLO WORLD'
