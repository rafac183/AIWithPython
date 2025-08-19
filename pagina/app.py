from flask import Flask, request, jsonify, redirect, render_template

app = Flask(__name__)

# Lista global de tareas
tareas = []
siguiente_id = 1

def agregar_tarea(texto):
    global siguiente_id

    tareas.append({'id': siguiente_id, 'texto': texto, 'hecho': False})

    siguiente_id += 1

def completar_tarea(id):
    for tarea in tareas:

        if tarea['id'] == id:

            tarea['hecho'] = True

            break

@app.route('/')

def index():

    # Ordenar tareas: incompletas primero, luego completadas

    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])

    return render_template('index.html', tareas=tareas_ordenadas)

@app.route('/api/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify(tareas)

@app.route('/agregar', methods=['POST'])

def agregar():

    texto_tarea = request.form.get('texto_tarea')

    if texto_tarea:

        agregar_tarea(texto_tarea)

    return redirect('/')

@app.route('/completar/<int:id>')

def completar(id):

    completar_tarea(id)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)