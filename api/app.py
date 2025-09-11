from flask import Flask, jsonify, request
from flask_cors import CORS
from flasgger import Swagger
from api.controllers.task_controller import task_bp
from api.controllers.user_controller import user_bp

app = Flask(__name__)

# Configuração do Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs"
}

template = {
    "swagger": "2.0",
    "info": {
        "title": "API - Done App",
        "description": "API do aplicativo de Gerenciamento de tarefas",
        "version": "1.0.1"
    }
}

# Inicializa Swagger com as configurações
swagger = Swagger(app, config=swagger_config, template=template)

# habilita CORS para todas as rotas
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], "allow_headers": "*"}})

# middleware para tratar OPTIONS (CORS preflight)
@app.after_request
def after_request(response):
    if request.method == "OPTIONS":
        response.status_code = 200
    return response

# registra o blueprint de tasks
app.register_blueprint(task_bp)
app.register_blueprint(user_bp)
