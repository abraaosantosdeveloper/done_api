from flask import Blueprint, jsonify, request
from workers.taskworker import get_all_tasks


task_bp = Blueprint('book', __name__)

@task_bp.route('/', methods=["GET", "OPTIONS"])
def get_tasks():
    if request.method == "OPTIONS":
        return jsonify({}), 200
        
    tasks = get_all_tasks()
    return jsonify(tasks), 200