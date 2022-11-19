from datetime import datetime
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

task_list = [
    {"id": 1, "text": "Despertar", "createdAt": datetime.now(), "doneAt": None},
    {"id": 2, "text": "Desayunar", "createdAt": datetime.now(), "doneAt": None},
    {"id": 3, "text": "Bañar", "createdAt": datetime.now(), "doneAt": None},
    {"id": 4, "text": "Salir", "createdAt": datetime.now(), "doneAt": None},
]

@app.route("/")
def index():
    return render_template("index.html", lista_tareas=task_list)

@app.route("/task", defaults={'id': None})
@app.route("/task/", defaults={'id': None})
@app.route("/task/<int:id>")
def task(id = None):
    # Si no me envias un ID, te regreso a index:
    if id == None:
        return redirect("/")
    # Si me envias un ID entonces trato de extraer la tarea con ese ID:
    task = None
    for t in task_list:
        if t['id'] == id:
            task = t
    # Si no existe la tarea con ese ID, lo regreso al index:
    if task == None:
        return redirect("/")
    # Si la tarea NO ESTA VACIA = la encontré. Entonces se la mando al template:
    return render_template("detail.html", task=task)

@app.route("/done", methods=["POST"])
def done():
    task_id = request.form.get("id")
    task = None
    indice = 0
    for t in task_list:
        if t['id'] == int(task_id):
            task = t
            break
        indice += 1
    # Si no existe la tarea con ese ID, lo regreso al index:
    if task == None:
        return redirect("/")
    # Si existe la tarea:
    task['doneAt'] = datetime.now()
    task_list[indice] = task
    return redirect("/task/" + str(task_id))