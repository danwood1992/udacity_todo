from flask import render_template, request, redirect, url_for
from models import User, TodoItem
from base import app, db

@app.route('/')
def index():
    users = User.query.all()
    tasks = TodoItem.query.all()
    return render_template('index.html', users=users, tasks=tasks)

@app.route('/add-user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    user = User(name=name, email=f"{name.lower()}@mail.com")
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/add-task', methods=['POST'])
def add_task():
    description = request.form.get('description')
    task = TodoItem(description=description)
    db.session.add(task)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/complete-task', methods=['POST'])
def complete_task():
    task_id = request.form.get('taskid')
    task = TodoItem.query.filter_by(id=task_id).first()
    print(f"debug: {task}")

    task.completed = True
    db.session.commit()

    return redirect(url_for('index'))

# @app.route('/undo-complete', methods=['POST'])
# def undo_complete_task():
#     task_id = request.form.get('taskid')
#     task = TodoItem.query.filter_by(id=task_id).first()
#     print(f"debug: {task}")

#     task.completed = False
#     db.session.commit()

#     return redirect(url_for('index'))

@app.route('/undo-complete', methods=['POST'])
def undo_complete_task():
    print(f"debug: {request.form}")
    task_id = request.form.get('taskid')
    task = TodoItem.query.filter_by(id=task_id).first()
    print(f"debug: {task}")
    print(f"debug: {task.completed}")
    task.undo_complete()

    return redirect(url_for('index'))

# @app.route('/delete-task', methods=['POST'])
# def delete_task():
#     task_id = request.form.get('taskid')
#     task = TodoItem.query.filter_by(id=task_id).first()

#     db.session.delete(task)
#     db.session.commit()

#     return redirect(url_for('index'))

@app.route('/delete-task', methods=['POST'])
def delete_task():
    task_id = request.form.get('taskid')
    task = TodoItem.query.filter_by(id=task_id).first()
    task.delete()

    return redirect(url_for('index'))