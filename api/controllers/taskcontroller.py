from flask import Blueprint, request, jsonify
from api.repositories.taskRepository import getTasks, newTask


task_bp = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods=['GET'])
def listar_tarefas():
    """
    Lista todas as tarefas
    ---
    tags:
      - Tarefas
    responses:
      200:
        description: Lista de tarefas encontradas
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: ID da tarefa
              nome_tarefa:
                type: string
                description: Nome da tarefa
              status:
                type: integer
                description: Status da tarefa (0 = pendente, 1 = concluída)
      400:
        description: Erro ao listar tarefas
        schema:
          type: object
          properties:
            message:
              type: string
              description: Erro ao listar tarefas (nada encontrado)
                    
      500:
        description: Erro interno do servidor
        schema:
          type: object
          properties:
            message:
              type: string
              description: Erro interno do servidor
      
    """
    return jsonify(getTasks())

@task_bp.route('/newTask', methods=['POST'])
def criar_tarefa():
    """
    Cria uma nova tarefa
    ---
    tags:
      - Tarefas
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome_tarefa:
              type: string
              description: Nome da tarefa a ser criada
    responses:
      201:
        description: Tarefa criada com sucesso
        schema:
          type: object
          properties:
            message:
              type: string
              description: Tarefa Criada com sucesso
      400:
        description: Erro ao criar tarefa
        schema:
          type: object
          properties:
            message:
              type: string
              description: Erro ao criar tarefa
      500:
        description: Erro interno do servidor
        schema:
          type: object
          properties:
            message:
              type: string
              description: Erro interno do servidor
    """
    info = request.get_json()
    result = newTask(info)
    if result:
        return jsonify({"message": "Tarefa criada com sucesso"}), 201
    return jsonify({"message": "Erro ao criar tarefa"}), 400