from flask import Blueprint, request, jsonify
from api.repositories.taskrepository import getTasks, newTask

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['POST'])
def realizar_login():
    """
        Função de login - Realiza login do usuário
        
        tags:
      - Tarefas
    responses:
      200:
        description: Informações de usuário logado
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: ID do usuário
              admin:
                type: integer
                description: Usuário administrador (0 = usuário padrão, 1 = usuário administrador)
              nome:
                type: string
                description: Nome do usuário
              nascimento:
                type: string
                description: Data de nascimento do usuário
              apelido:
                type: string
                description: Nickname de usuário(Apelido)
              email:
                type: string
                description: Email cadastrado para o usuário
              hash_senha:
                type: string
                description: hash da senha cadastrada pelo usuário
                        
    """
    
    # info = request.get_json()
    # result = userLogin(info)
    # if result:
    #     return jsonify({"message": "Login realizado!"}), 201
    # return jsonify({"message": "Erro ao realizar login..."}), 400
    pass

