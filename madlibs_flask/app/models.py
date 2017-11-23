from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    stories = db.relationship('Story', backref='author', lazy='dynamic')

    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Story %r>' % (self.body)        