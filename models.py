from base import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    
    def __repr__(self):
        return f'User ID: {self.id}, name: {self.name}'
    
class TodoList(db.Model):
    __tablename__ = 'todo_lists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    tasks = db.relationship('TodoItem', backref='list', lazy=True)
  
    def __repr__(self):
        return f'Todo List: {self.name}'
    
    def add_task(self, description):
        task = TodoItem(description=description, list_id=self.id)
        db.session.add(task)
        db.session.commit()

    def delete(self):
        todo_items = TodoItem.query.all()
        print(f"debug all todo items: {todo_items}")
        for item in todo_items:
            if item.list_id == self.id:
                print("debug item: List id match")
                item.delete()
        db.session.delete(self)
        db.session.commit()

        
    
class TodoItem(db.Model):
    __tablename__ = 'todo_items'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    important = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todo_lists.id'), nullable=False)

    def __repr__(self):
        return f'Todo Item: {self.description}'
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def undo_complete(self):
        self.completed = False
        db.session.commit()

    def complete(self):
        self.completed = True
        db.session.commit()

    def toggle_important(self):
        self.important = not self.important
        db.session.commit()

    def update(self, description):
        self.description = description
        db.session.commit()

