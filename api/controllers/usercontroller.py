from flask import Blueprint, request, jsonify
from api.repositories.taskrepository import getTasks, newTask

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['POST'])
def realizar_login():
    """
    Função de login - Realiza login do usuário
    ---
    tags:
      - Usuários
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              description: Email cadastrado para o usuário
            senha:
              type: string
              description: Senha cadastrada pelo usuário
    responses:
      200:
        description: Informações de usuário logado
        schema:
          type: array
          items:
            type: object
            properties:
              email:
                type: string
                description: Email cadastrado para o usuário
              hash_senha:
                type: string
                description: Hash da senha cadastrada pelo usuário
      400:
        description: Erro ao realizar login
        schema:
          type: array
          items:
            type: object
            properties:
              error:
                type: string
                description: Informações não encontradas
      401:
        description: Credenciais inválidas
        schema:
          type: array
          items:
            type: object
            properties:
              error:
                type: string
                description: Informações inválidas
      500:
        description: Erro interno do servidor
        schema:
          type: array
          items:
            type: object
            properties:
              error:
                type: string
                description: Erro interno do servidor         
    """
    
    # info = request.get_json()
    # result = userLogin(info)
    # if result:
    #     return jsonify({"message": "Login realizado!"}), 201
    # return jsonify({"message": "Erro ao realizar login..."}), 400
    pass

