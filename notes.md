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