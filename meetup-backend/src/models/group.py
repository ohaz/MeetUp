from database import db
import string, time, math, random


class Group(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    uid = db.Column(db.String(265))

    def __init__(self, name):
        self.name = name
        self.uid = unique_id(prefix='G')

    def __repr__(self):
        return '<Group {} - {}>'.format(self.uid, self.name)


def unique_id(prefix: str ='', more_entropy: bool =False):
    m: float = time.time()
    unique_id_: str = '%8x%05x' % (int(math.floor(m)), int((m - math.floor(m)) * 1000000))
    if more_entropy:
        valid_chars: list = list(set(string.hexdigits.lower()))
        entropy_string: str = ''
        for i in range(0, 10, 1):
            entropy_string += random.choice(valid_chars)
            unique_id_ = unique_id_ + entropy_string
            unique_id_ = prefix + unique_id_
    return unique_id_
