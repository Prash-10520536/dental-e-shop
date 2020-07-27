from dental import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer)
    username = db.Column(db.String(30), unique=True, nullable=False)
    address = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()