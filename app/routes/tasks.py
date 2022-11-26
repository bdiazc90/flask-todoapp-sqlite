from flask import Blueprint, render_template, redirect, request
from app.db import db
from app.models.task import Task
from datetime import datetime

task_router = Blueprint("task_router", __name__)

#
# Inicio de las rutas del app (sección tareas):
#
@task_router.route("/")
def index():
    task_list = Task.query.all() # SELECT * FROM task
    return render_template("index.html", lista_tareas=task_list)

@task_router.route("/add", methods=["POST"])
def add():
    task_text = request.form.get("text") # Recupero lo que viene en el input del form
    if task_text == "" or task_text == None:
        return redirect("/")
    
    newTask = Task(text=task_text, createdAt=datetime.now())
    db.session.add(newTask) # Por dentro creará el SQL COMMAND: INSERT
    db.session.commit() # Envia los SQL COMMAND al motor de DB.
    return redirect("/")


@task_router.route("/update/<int:id>", methods=["PUT"])
def update(id):
    task = Task.query.get(id)
    task.text = request.form.get("text")
    db.session.commit()
    return task.dict(), 200


@task_router.route("/task", defaults={'id': None})
@task_router.route("/task/", defaults={'id': None})
@task_router.route("/task/<int:id>")
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

@task_router.route("/done", methods=["POST"])
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

@task_router.route("/delete/<int:id>")
def delete(id):
    task = Task.query.get(id)
    if task == None:
        return redirect("/")
    # Si existe la tarea:
    task.deletedAt = datetime.now()
    db.session.commit()
    return redirect("/task/" + str(id))