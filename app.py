from flask import render_template, request, redirect, url_for
from models import User, TodoItem
import random
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

@app.route('/undo-complete', methods=['POST'])
def undo_complete_task():
    task_id = request.form.get('taskid')
    task = TodoItem.query.filter_by(id=task_id).first()
    print(f"debug: {task}")

    task.completed = False
    db.session.commit()

    return redirect(url_for('index'))



if __name__ == '__main__': 
   app.run(host="0.0.0.0", port=5125, debug=True)


