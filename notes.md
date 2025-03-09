# Topics to understand in Flask

my reference video on youtube [link](https://www.youtube.com/watch?v=oQ5UfJqW5Jo&t=7109s)

## Circular imports issue in Flask
understanding the circular imports
in this project we have the following python files
1. `run.py` import the app create function
2. `app.py` import the routes from `routes,.py`
3. `models.py` imports the db from `app.py`
4. `routes.py` imports the models from `models.py`


in simple this is a circular imports that never end in case we 
didn't create the `run.apy` and we define only the create_app function 
in app.py

`app.py` > `models.py` > `routes.py` > `app.py`

## Setting up the project
1. we first start with installing the required packages for flask
```
pip3 install flask flask-sqlalchemy flask-migrate
```
2. we also install `psycopg2` in case we are using `PostgreSQL` as
database manager
```
pip3 install psycopg2
```
## Project Structure
### app.py
here where we should avoid the cicular imports
### models.py
- In Flask application we don't have database but we have classes. 
- When we connect to the database we connect to tables in that database (sqlite, postgresql, mysql,....) no matter what type of database. 
- SqlAlchemy in Flask which is ORM (Object Relational Mapper) converts (migrate) the classes into database tables, so by that it connects the database with the flask application, where we can do whatever we want on the classes (delete, update, insert,....) sql alchemy will convert all of those actions to the database (that is supoer cool)
- also we can select tables from the database and sql alchemy will convert those tables into classes, we can edit on the flask app itself.
- once we define our models, we need to import the `models.py` file into the `app.py`

### run.py
here where we run the application 


### routes.py
in this file we define the application routes 
the navigation of the web application


## Connecting to the database in app.py
in order to connect to the database using sqlalchemy 
we have to follow the syntax
```
dialect://username:password@host:port/database
```
in my case, I want to connect to `postgresql`, in this case the following:

- **dialect**: postgresql
- **username**: database username
- **password**: database password
- **host**: localhost
- **port**: the database port on localhost `5432`
- **database**: the database name I want to connect to
```
postgresql://username:password@localhost:5432/databasename
```
### run the application with the connected database
to do this we have to do the following:
1. we run this command _**once**_ in the beginning only, 
in the terminal we run this in the same directory 
of our application in order to initiate the database
```
python -m flask db init
```
2. we do them the migration to the database
```
python -m flask db migrate
```
3. then we do the last command 
```
python -m flask db upgrade
```

## Design Pattern
the design pattern used in this app is the `Factory Pattern`

## Flask Authentication

1. we will have a `User` class
2. build the authentication for the `User` class
3. the operation here we are going to do is
   1. login a user 
   2. register or sign up a user
   3. keep a user logged in
   4. differentiate between users, and checking which user is sending the requests

**For this we have to install the following:**

1. we need to install external packages 
   1. `flask-login`
   2. `flask-bcrypt` this package is going to be used in order to hash
   the user's password when adding a user to the database,
   so we keep all the secrets hashed and secured in the database
   and when dealing with it within the code-base
```
pip3 install flask-login flask-bcrypt
```

2. now we have to import the packages inside the `app.py` file 
```
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
```

3. inside the `models.py` we need to import the following
```
from flask_login import UserMixin
```
4. in the `app.py` we have to define the secret of the user session


##### Flask Login Does not implement the logic of the loggin procedure
this means that the way we want to log_in the user to the app like
1. with password
2. with email
3. with another security measure

is not done here, this package for managing the log_in process nothing else
1. login the user
2. keep the user logged in
3. logout the user
 

## Blueprints in Flask Applications
Blueprints in Flask Apps is the idea of turning the app into different modules/components
where its module/component is a separate entity.

we start first by creating a folder within the root folder of the app, and we package it with the file 
`__init__.py` and other app-related files like `app.py`

the `run.py` is in the root folder of the app.

## Errors and Solutions

1. while trying migrating the columns data the fllowing error I received
```
ERROR [flask_migrate] Error: Target database is not up to date.
```
to solve this issue, [stackoverflow](https://stackoverflow.com/questions/17768940/target-database-is-not-up-to-date)
```
python -m flask db stamp head
python -m flask db migrate
python -m flask db upgrade
```


## References

[SQLAlchemy Configuration Reference](https://flask-sqlalchemy.readthedocs.io/en/stable/config/)

[PostgreSQL-SQLAlchemy](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html)

[SQL Datatype Objects in SQLAlchemy](https://docs.sqlalchemy.org/en/20/core/types.html)

