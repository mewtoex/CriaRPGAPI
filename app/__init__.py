from flask import Flask
from app.routes import api_blueprint
from app.config import Config

def create_app():
    app = Flask(__name__)
    
    # Configurações da aplicação
    app.config.from_object(Config)
    
    # Registra as rotas
    app.register_blueprint(api_blueprint)
    
    return app