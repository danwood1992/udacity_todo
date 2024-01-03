from flask import render_template, request, redirect, url_for, jsonify
from models import User, TodoItem, TodoList
from base import app, db

def get_task(request):
    task_id = request.form.get('taskid')
    task = TodoItem.query.filter_by(id=task_id).first()
    return task

@app.route('/')
def index():
    users = User.query.all()
    lists = TodoList.query.all()
    tasks = TodoItem.query.all()
    return render_template('index.html', users=users,lists=lists, tasks=tasks)

@app.route('/lists/create', methods=['POST'])
def add_list():
    name = request.get_json()['name']
    list = TodoList(name=name)
    db.session.add(list)
    db.session.commit()
    return jsonify({
        'id': list.id,
        'name': list.name
    })
    

@app.route('/add-task', methods=['POST'])
def add_task():
    list_id = request.form.get('listid')
    description = request.form.get('description')
    task = TodoItem(description=description, list_id=list_id)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete-task', methods=['POST'])
def complete_task():
    task = get_task(request)
    task.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/undo-complete', methods=['POST'])
def undo_complete_task():
    task = get_task(request)
    task.undo_complete()
    return redirect(url_for('index'))

@app.route('/delete-task', methods=['POST'])
def delete_task():
    task = get_task(request)
    task.delete()
    return redirect(url_for('index'))

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/add-user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    user = User(name=name, email=f"{name.lower()}@mail.com")
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('users'))
