from application import application
from models.group_user import group_user_association
from uuid import uuid4


class Group(application.db.Model):
    id = application.db.Column(application.db.Integer, primary_key=True)
    name = application.db.Column(application.db.String(50))
    uid = application.db.Column(application.db.String(36))
    users = application.db.relationship('User', secondary=group_user_association, backref="groups")

    def __init__(self, name):
        self.name = name
        self.uid = 'G' + uuid4().hex

    def __repr__(self):
        return '<Group {} - {}>'.format(self.uid, self.name)

    def __str__(self):
        return self.uid

    def to_dict(self):
        return {'name': self.name, 'uid': self.uid}

    def all(self):
        d = self.to_dict()
        d['users'] = [u.to_dict() for u in self.users]
        return d
