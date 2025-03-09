from blueprints.app import db

class Todos(db.Model):
    __tablename__ = 'todos'

    tuid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    done = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        if self.done:
            return f'Todo: {self.title} is done'
        else:
            return f'Todo: {self.title} is not done yet'

    def get_tuid(self):
        return self.tuid