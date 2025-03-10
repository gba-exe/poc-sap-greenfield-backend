from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.transactions import transactions_bp

    app.register_blueprint(transactions_bp, url_prefix='/transactions')

    return app
