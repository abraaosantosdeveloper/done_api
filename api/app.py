from flask import Flask, jsonify, request
from flask_cors import CORS
from api.controllers.taskcontroller import task_bp

app = Flask(__name__)

# habilita CORS para todas as rotas
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], "allow_headers": "*"}})

# middleware para tratar OPTIONS (CORS preflight)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    
    if request.method == "OPTIONS":
        response.status_code = 200
    return response

# registra o blueprint de tasks
app.register_blueprint(task_bp)

