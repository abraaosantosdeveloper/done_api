from flask import Blueprint, jsonify, request
from api.workers.taskworker import get_all_tasks


task_bp = Blueprint('task', __name__)

@task_bp.route('/', methods=["GET", "OPTIONS"])
def get_tasks():
    if request.method == "OPTIONS":
        return jsonify({}), 200
        
    tasks = get_all_tasks()
    return jsonify(tasks), 200

@task_bp.route('/', methods=["POST", "OPTIONS"])
def create_task():
    if request.method == "OPTIONS":
        return jsonify({}), 200
    
    data = request.get_json()
    if data is None or 'nome_tarefa' not in data:
        return jsonify({"error": "Requisição deve ser JSON válido com Content-Type: application/json"}), 400
    
    result, status_code = newTask(data)
    return jsonify(result), status_code