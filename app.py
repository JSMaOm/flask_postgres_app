from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

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

    # define the strong session key
    app.secret_key = 'WHATEVERSTRONGKEY'

    db.init_app(app)
    # define the login manager
    login_manager = LoginManager()
    # initiate the login manager
    login_manager.init_app(app)

    from models import User
    # here we give the login_manager the method
    # to tell him what to do when loading a user
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)

    # to change the behavior of redirection for unauthorized users
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for('index'))

    # define the bcrypt object
    # we pass the bcrypt object also to register_routes function
    # because we want to use it in hashing the passwords for users
    bcrypt = Bcrypt(app)

    # here we import the routes
    from routes import register_routes
    register_routes(app, db, bcrypt)

    migrate = Migrate(app, db)

    return app