from application import application

db = application.db

group_user_association = db.Table('association', db.Model.metadata,
                                  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                                  db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
                                  )
