from base import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    
    def __repr__(self):
        return f'User ID: {self.id}, name: {self.name}'
    
class TodoItem(db.Model):
    __tablename__ = 'todo_items'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    important = db.Column(db.Boolean, nullable=False, default=False)

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

    
# class TodoList(db.Model):
#     __tablename__ = 'todo_lists'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(), nullable=False)
#     items = db.relationship('TodoItem', backref='list', lazy=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
#     def __repr__(self):
#         return f'Todo List: {self.name}'