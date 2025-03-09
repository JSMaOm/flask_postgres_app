from flask import render_template, redirect, request, url_for, Blueprint

from blueprints.app import db
from blueprints.todos.models import Todos

todos = Blueprint('todos', __name__, template_folder='templates')

@todos.route('/')
def index():
    todos = Todos.query.all()
    return render_template('todos/index.html', todos=todos)

@todos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('todos/create.html')
    elif request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        done = True if 'done' in request.form.keys() else False

        description = description if description != '' else None

        todo = Todos(title=title, description=description, done=done)

        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todos.index'))
