from flask import render_template, request

# here we import the models we want to use
from models import Person

# to avoid the circular imports we use a function here
def register_routes(app, db):

    # the / means this is the default page in this case it is index
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            people = Person.query.all()
            return render_template('index.html', people = people)
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
            return render_template('index.html', people=people)

    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        # we query the person with the passed pid and delete it
        Person.query.filter(Person.pid == pid).delete()
        # then we commit the db session
        db.session.commit()

        people = Person.query.all()
        return render_template('index.html', people=people)

    @app.route('/details/<pid>')
    def details(pid):
        person = Person.query.filter(Person.pid == pid).first()
        return render_template('details.html', person=person)

