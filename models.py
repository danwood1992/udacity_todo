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