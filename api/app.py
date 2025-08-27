from flask import Flask, jsonify, request
from flask_cors import CORS
from flasgger import Swagger
from api.controllers.taskcontroller import task_bp

app = Flask(__name__)

# habilita CORS para todas as rotas
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], "allow_headers": "*"}})
swagger = Swagger(app)


# middleware para tratar OPTIONS (CORS preflight)
@app.after_request
def after_request(response):
    if request.method == "OPTIONS":
        response.status_code = 200
    return response

# registra o blueprint de tasks
app.register_blueprint(task_bp)

