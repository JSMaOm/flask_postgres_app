from blueprints.app import db

class Person(db.Model):
    __tablename__ = 'people'

    puid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.String)

    def __repr__(self):
        return f'{self.name} with age {self.age}'

    def get_tuid(self):
        return self.puid