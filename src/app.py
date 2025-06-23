from flask import Flask, request

app = Flask(__name__)

todos = [{'label': 'My first task', 'done': False},
         {'label': 'My second task', 'done': False}]

@app.route('/todos', methods=['GET', 'POST'])
def todos_endpoint():
    response_body = {}
    if request.method == 'GET':
        response_body['message'] = 'Listado de Todos'
        response_body['results'] = todos
        return response_body
    if request.method == 'POST':
        data = request.json
        todos.append(data)
        response_body['message'] = 'Todo agregado correctamente'
        response_body['results'] = todos
        return response_body, 200

@app.route('/todos/<int:position>', methods=['GET', 'PUT', 'DELETE'])
def todo_endpoint(position):
    response_body = {}
    if position >= len(todos):
        response_body['message'] = f'El ToDo {position} no existe'
        response_body['results'] = {}
        return response_body, 404
    if request.method == 'DELETE':
        del todos[position]
        response_body['message'] = f'El ToDo {position} fue eliminado correctamente'
        response_body['results'] = todos
        return response_body, 200
    if request.method == 'GET':
        response_body['message'] = f'Los datos del ToDo {position} son los siguientes'
        response_body['results'] = todos[position]
        return response_body, 200
    if request.method == 'PUT':
        data = request.json
        todos[position] = data
        response_body['message'] = f'Los datos de ToDo {position} fueron modificados con éxito'
        response_body['results'] = todos[position]
        return response_body, 200
    
    response_body['message'] = f'Error desconocido'
    response_body['results'] = {}
    return response_body, 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)