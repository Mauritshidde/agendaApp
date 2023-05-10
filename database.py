class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    hash = db.Column(db.String, nullable=False)
    salt = db.Column(db.String, nullable=False)
