from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:dogsarecool@localhost:5432/flask_db"

    db.init_app(app)

    # import and register all blueprints
    from blueprints.core.routes import core
    from blueprints.todos.routes import todos
    from blueprints.people.routes import people

    app.register_blueprint(core, url_prefix='/')
    app.register_blueprint(todos, url_prefix='/todos')
    app.register_blueprint(people, url_prefix='/people')

    migrate = Migrate(app, db)

    return app