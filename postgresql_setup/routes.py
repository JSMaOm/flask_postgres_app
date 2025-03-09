from flask import render_template, request, redirect, url_for
# we import from the flask_login what we need to deal with the user login
from flask_login import login_user, logout_user, current_user, login_required

# here we import the models we want to use
from postgresql_setup.models import Person, User

# to avoid the circular imports we use a function here
def register_routes(app, db, bcrypt):
    # ----------------- Person Routes -----------------
    # the / means this is the default page in this case it is index
    @app.route('/person/', methods=['GET', 'POST'])
    def index_person():
        if request.method == 'GET':
            people = Person.query.all()
            return render_template('index_person.html', people = people)
        elif request.method == 'POST':
            name = request.form.get('name')
            age = int(request.form.get('age'))
            job = request.form.get('job')

            # we create a person instance from Person
            person = Person(name=name, age=age, job=job)

            # now we add person to the database
            db.session.add(person)
            db.session.commit()

            people = Person.query.all()
            return render_template('index_person.html', people=people)

    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        # we query the person with the passed pid and delete it
        Person.query.filter(Person.pid == pid).delete()
        # then we commit the db session
        db.session.commit()

        people = Person.query.all()
        return render_template('index_person.html', people=people)

    @app.route('/details/<pid>')
    def details(pid):
        person = Person.query.filter(Person.pid == pid).first()
        return render_template('details.html', person=person)

    # -----------------------------------------------
    # ----------------- User Routes -----------------

    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return render_template('index_users.html')
        else:
            return render_template('index_users.html')

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            # here where we have to hash the password before adding the user to the database
            # for postgresql we have to decode the string before we save it to the database
            # the reason for this is we lose the hash salt and the string will be saved in utf8 to the database
            # we lose the hash itself
            # this is one way to solve it, other way is to change the type of the password column in the database table
            hashed_password = bcrypt.generate_password_hash(password).decode('utf8')

            user = User(username=username, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            # and now we redirect the user to the index page or whatever page we want
            return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter(User.username==username).first()
            print(user.password)
            print(bcrypt.generate_password_hash(password))
            if bcrypt.check_password_hash(user.password, password):
                print(bcrypt.check_password_hash(user.password, password))
                login_user(user)
                return redirect(url_for('index'))
            else:
                return 'Failed Login'

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))

    # in case we have some endpoints we want only the authenticated users
    # to be able to log_in to
    # for this we need to require log_in
    @app.route('/secret')
    @login_required
    def secret():
        return 'Only for Authorized Users!'