from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.taskcontroller import task_bp

app = Flask(__name__)

# habilita CORS para todas as rotas
CORS(app, resources={r"/*": {"origins": "*"}})

# middleware para tratar OPTIONS (CORS preflight)
@app.after_request
def after_request(response):
    if request.method == "OPTIONS":
        response.status_code = 200
    return response

# registra o blueprint de tasks
app.register_blueprint(task_bp)

# só roda com app.run localmente
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
