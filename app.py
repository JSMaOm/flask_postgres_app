from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# here we define the database object that we want to 
# import into the models.py file 
db = SQLAlchemy()

# This function creates the app and returns it as an object
# in this way, it will be executed when importing the app.py
# in any file
def create_app():
    app = Flask(__name__, template_folder="templates")
    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://username:password@localhost:5432/databasename"
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:dogsarecool@localhost:5432/flask_db"

    db.init_app(app)
    # here we import the routes
    from routes import register_routes
    register_routes(app, db)

    migrate = Migrate(app, db)

    return app