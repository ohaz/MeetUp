from application import application
from uuid import uuid4


class User(application.db.Model):

    id = application.db.Column(application.db.Integer, primary_key=True)
    uid = application.db.Column(application.db.String(36))

    def __init__(self):
        self.uid = 'U' + uuid4().hex

    def __repr__(self):
        return '<User {}>'.format(self.uid)

    def __str__(self):
        return self.uid

    def to_dict(self):
        return {'uid': self.uid}
