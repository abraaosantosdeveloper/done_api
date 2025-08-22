from flask import Flask, jsonify, request
from flask_cors import CORS

from controllers.taskcontroller import task_bp

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

def after_request(response):
    if request.method == "OPTIONS":
        response.status_code = 200
    return response

app.register_blueprint(task_bp)

