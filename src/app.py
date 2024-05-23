# Añade el método jsonify a tu importación de Flask
from flask import Flask, jsonify, request
app = Flask(__name__)

# Supongamos que tienes tus datos en la variable some_data
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    # Puedes convertir esa variable en una cadena json de la siguiente manera
    json_todos = jsonify(todos)

    # Y luego puedes devolverlo al front-end en el cuerpo de la respuesta de la siguiente manera
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body_json = request.json
    todos.append(request_body_json)
    json_todos = jsonify(todos)
    
    return json_todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position - 1]
    json_todos = jsonify(todos)
    return json_todos
    


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)