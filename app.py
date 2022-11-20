from datetime import datetime
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Esta es nuestra DB temporal hecha en python:
# task_list = [
#     {"id": 1, "text": "Despertar", "createdAt": datetime.now(), "doneAt": None},
#     {"id": 2, "text": "Desayunar", "createdAt": datetime.now(), "doneAt": None},
#     {"id": 3, "text": "Bañar", "createdAt": datetime.now(), "doneAt": None},
#     {"id": 4, "text": "Salir", "createdAt": datetime.now(), "doneAt": None},
# ]

# Esta es nuestra VERDADERA DB en SQLITE:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) # INT
    text = db.Column(db.String(200)) # VARCHAR(200)
    createdAt = db.Column(db.DateTime(timezone=False))
    doneAt = db.Column(db.DateTime(timezone=False))
    deletedAt = db.Column(db.DateTime(timezone=False))


#
# Inicio de las rutas del app:
#
@app.route("/")
def index():
    task_list = Task.query.all() # SELECT * FROM task
    return render_template("index.html", lista_tareas=task_list)

@app.route("/add", methods=["POST"])
def add():
    task_text = request.form.get("text") # Recupero lo que viene en el input del form
    if task_text == "" or task_text == None:
        return redirect("/")
    
    newTask = Task(text=task_text, createdAt=datetime.now())
    db.session.add(newTask) # Por dentro creará el SQL COMMAND: INSERT
    db.session.commit() # Envia los SQL COMMAND al motor de DB.
    return redirect("/")


# @app.route("/fix")
# def fix():
#     error_task = Task.query.get(1)
#     error_task.createdAt = datetime.now()    
#     db.session.commit()
#     return redirect("/")


@app.route("/task", defaults={'id': None})
@app.route("/task/", defaults={'id': None})
@app.route("/task/<int:id>")
def task(id = None):
    # Si no me envias un ID, te regreso a index:
    if id == None:
        return redirect("/")
    # Si me envias un ID entonces trato de extraer la tarea con ese ID:
    task = Task.query.get(id)
    if task == None:
        return redirect("/")
    # Si la tarea NO ESTA VACIA = la encontré. Entonces se la mando al template:
    return render_template("detail.html", task=task)

@app.route("/done", methods=["POST"])
def done():
    task_id = request.form.get("id")
    next = request.form.get("next")
    task = Task.query.get(task_id)
    if task == None:
        return redirect("/")
    # Si existe la tarea:
    task.doneAt = datetime.now()
    db.session.commit()
    # finish:
    if next != None:
        return redirect(next)
    return redirect("/task/" + str(task_id))

@app.route("/delete/<int:id>")
def delete(id):
    task = Task.query.get(id)
    if task == None:
        return redirect("/")
    # Si existe la tarea:
    task.deletedAt = datetime.now()
    db.session.commit()
    return redirect("/task/" + str(id))

# Crear la tabla por unica vez:
db.init_app(app)
with app.app_context():
    db.create_all() # Buscar las clases que heredan de "db.Model" y las va a crear en caso no existan.