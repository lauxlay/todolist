from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@"+ os.environ['DB_HOST'] +":5432/postgres"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class TodoModel(db.Model):
    __tablename__ = 'todolist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Todo {self.name}>"

@app.route('/api/actuator')
def testdb():
    try:
        TodoModel.query.all()
        return {"status": "UP"}
    except:
        return {"status": "DOWN"}, 500

#def actuator():
#    return {"status": "UP"}

@app.route('/todos', methods=['POST', 'GET'])
def handle_todos():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_todo = TodoModel(name=data['name'])
            db.session.add(new_todo)
            db.session.commit()
            return {"message": f"Todo {new_todo.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        todos = TodoModel.query.all()
        results = [
            {
                "name": todo.name,
            } for todo in todos]

        return {"count": len(results), "todo": results}

if __name__ == '__main__':
    app.run(debug=True)