from flask import Blueprint
from flask_cors import CORS 
from app.controler.user_controler import login_controller_user, save_controller_user, update_controller_user

api_blueprint = Blueprint('api', __name__)

CORS(api_blueprint, resources={r"/*": {"origins": "*"}})

@api_blueprint.route('/login', methods=['POST'])  
def login():
    return login_controller_user()

@api_blueprint.route('/user/new', methods=['POST'])  
def save_user():
    return save_controller_user()

@api_blueprint.route('/user/update', methods=['POST'])  
def update_user():
    return update_controller_user()