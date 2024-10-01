from flask import Blueprint
from flask_cors import CORS 
from app.controler.chassi_controler import chassi_list, save_controller_chassi, update_controller_chassi
from app.controler.cria_controler import busca_cria_com_relacoes, save_controller_cria, update_controller_cria
from app.controler.elemento_controler import elemento_list, save_controller_elemento, update_controller_elemento
from app.controler.especial_controler import especial_list, especial_list_type, save_controller_especial, update_controller_especial
from app.controler.fraquezas_type_controler import fraqueza_list, fraqueza_list_type, save_controller_fraqueza, update_controller_fraqueza
from app.controler.motivo_controler import motivo_list, motivo_list_type, save_controller_motivo, update_controller_motivo
from app.controler.objetivo_controler import objetivo_list, objetivo_list_type, save_controller_objetivo, update_controller_objetivo 
from app.controler.objeto_controler import objeto_list, objeto_list_type, save_controller_objeto, update_controller_objeto
from app.controler.pecas_controler import pecas_list, pecas_list_type, save_controller_pecas, update_controller_pecas
from app.controler.pessonalidade_controler import personalidade_list, save_controller_personalidade, update_controller_personalidade
from app.controler.pivete_controler import busca_pivete_por_user, save_controller_pivete, update_controller_pivete
from app.controler.pivete_type_controler import pivete_type_list, save_pivete_type, update_pivete_type
from app.controler.poderes_controler import poderes_list, poderes_list_type, save_controller_poderes, update_controller_poderes
from app.controler.quarto_controler import quarto_list, quarto_list_type, save_controller_quarto, update_controller_quarto
from app.controler.tecnicas_controler import tecnica_list, tecnica_list_filter, save_controller_tecnica,update_controller_tecnica
from app.controler.vinculo_controler import vinculo_list, vinculo_list_type, save_controller_vinculo, update_controller_vinculo
from app.controler.user_controler import login_controller_user, save_controller_user, update_controller_user
from app.decorators import token_required

api_blueprint = Blueprint('api', __name__)

CORS(api_blueprint, resources={r"/*": {"origins": "*"}})

#region User
@api_blueprint.route('/login', methods=['POST'])  
def login():
    return login_controller_user()

@api_blueprint.route('/user/new', methods=['POST'])
@token_required  
def save_user():
    return save_controller_user()

@api_blueprint.route('/user/update', methods=['POST']) 
@token_required 
def update_user():
    return update_controller_user()
#endregion

#region Vinculo
@api_blueprint.route('/vinculo/list', methods=['POST'])  
@token_required
def list_vinculos():
    return vinculo_list()

@api_blueprint.route('/vinculo/listtype', methods=['POST'])  
@token_required
def list_vinculo_types():
    return vinculo_list_type()

@api_blueprint.route('/vinculo/new', methods=['POST'])  
@token_required
def save_vinculo():
    return save_controller_vinculo()

@api_blueprint.route('/vinculo/update', methods=['POST'])  
@token_required
def update_vinculo():
    return update_controller_vinculo()
#endregion

#region Tecnica
@api_blueprint.route('/tecnica/list', methods=['POST']) 
@token_required 
def list_tecnicas():
    return tecnica_list()

@api_blueprint.route('/tecnica/tecnicatype', methods=['POST'])  
@token_required
def list_tecnica_types():
    return tecnica_list_filter()

@api_blueprint.route('/tecnica/new', methods=['POST'])  
@token_required
def save_tecnica():
    return save_controller_tecnica()

@api_blueprint.route('/tecnica/update', methods=['POST'])  
@token_required
def update_tecnica():
    return update_controller_tecnica()
#endregion

#region Quarto
@api_blueprint.route('/quarto/list', methods=['POST'])  
@token_required
def list_quartos():
    return quarto_list()

@api_blueprint.route('/quarto/listtype', methods=['POST'])  
@token_required
def list_quarto_types():
    return quarto_list_type()

@api_blueprint.route('/quarto/new', methods=['POST'])  
@token_required
def save_quarto():
    return save_controller_quarto()

@api_blueprint.route('/quarto/update', methods=['POST'])  
@token_required
def update_quarto():
    return update_controller_quarto()
#endregion

#region Poderes
@api_blueprint.route('/poderes/list', methods=['POST'])  
@token_required
def list_poderes():
    return poderes_list()

@api_blueprint.route('/poderes/listtype', methods=['POST'])  
@token_required
def list_poderes_types():
    return poderes_list_type()

@api_blueprint.route('/poderes/new', methods=['POST']) 
@token_required 
def save_poder():
    return save_controller_poderes()

@api_blueprint.route('/poderes/update', methods=['POST'])  
@token_required
def update_poder():
    return update_controller_poderes()
#endregion

#region Pivete type
@api_blueprint.route('/pivetetype/list', methods=['POST'])  
@token_required
def list_pivete_types():
    return pivete_type_list()

@api_blueprint.route('/pivetetype/new', methods=['POST'])  
@token_required
def save_pivete_type():
    return save_pivete_type()

@api_blueprint.route('/pivetetype/update', methods=['POST'])  
@token_required
def update_pivete_type():
    return update_pivete_type()
#endregion

#region Pivete
@api_blueprint.route('/pivete/list', methods=['POST'])  
@token_required
def list_pivetes():
    return busca_pivete_por_user() 

@api_blueprint.route('/pivete/new', methods=['POST'])  
@token_required
def save_pivete():
    return save_controller_pivete()

@api_blueprint.route('/pivete/update', methods=['POST'])  
@token_required
def update_pivete():
    return update_controller_pivete()
#endregion

#region Pessonalidade
@api_blueprint.route('/pessonalidade/list', methods=['POST'])  
@token_required
def list_personalidades():
    return personalidade_list()

@api_blueprint.route('/pessonalidade/new', methods=['POST'])  
@token_required
def save_personalidade():
    return save_controller_personalidade()

@api_blueprint.route('/pessonalidade/update', methods=['POST'])  
@token_required
def update_personalidade():
    return update_controller_personalidade()
#endregion

#region Pecas
@api_blueprint.route('/pecas/list', methods=['POST'])  
@token_required
def list_pecas():
    return pecas_list()

@api_blueprint.route('/pecas/listtype', methods=['POST'])  
@token_required
def list_pecas_types():
    return pecas_list_type()

@api_blueprint.route('/pecas/new', methods=['POST'])  
@token_required
def save_pecas():
    return save_controller_pecas()

@api_blueprint.route('/pecas/update', methods=['POST'])  
@token_required
def update_pecas():
    return update_controller_pecas()
#endregion

#region Objeto
@api_blueprint.route('/objeto/list', methods=['POST'])  
@token_required
def list_objetos():
    return objeto_list()

@api_blueprint.route('/objeto/listtype', methods=['POST'])  
@token_required
def list_objeto_types():
    return objeto_list_type()

@api_blueprint.route('/objeto/new', methods=['POST'])  
@token_required
def save_objeto():
    return save_controller_objeto()

@api_blueprint.route('/objeto/update', methods=['POST'])  
@token_required
def update_objeto():
    return update_controller_objeto()
#endregion

#region Objetivo
@api_blueprint.route('/objetivo/list', methods=['POST'])  
@token_required
def list_objetivos():
    return objetivo_list()

@api_blueprint.route('/objetivo/listtype', methods=['POST'])  
@token_required
def list_objetivo_types():
    return objetivo_list_type()

@api_blueprint.route('/objetivo/new', methods=['POST'])  
@token_required
def save_objetivo():
    return save_controller_objetivo()

@api_blueprint.route('/objetivo/update', methods=['POST'])  
@token_required
def update_objetivo():
    return update_controller_objetivo()
#endregion

#region Motivo
@api_blueprint.route('/motivo/list', methods=['POST'])  
@token_required
def list_motivos():
    return motivo_list()

@api_blueprint.route('/motivo/listtype', methods=['POST'])  
@token_required
def list_motivo_types():
    return motivo_list_type()

@api_blueprint.route('/motivo/new', methods=['POST'])  
@token_required
def save_motivo():
    return save_controller_motivo()

@api_blueprint.route('/motivo/update', methods=['POST'])  
@token_required
def update_motivo():
    return update_controller_motivo()
#endregion

#region Fraquezas
@api_blueprint.route('/fraquezas/list', methods=['POST'])  
@token_required
def list_fraquezas():
    return fraqueza_list()

@api_blueprint.route('/fraquezas/listtype', methods=['POST'])  
@token_required
def list_fraquezas_types():
    return fraqueza_list_type()

@api_blueprint.route('/fraquezas/new', methods=['POST'])  
@token_required
def save_fraqueza():
    return save_controller_fraqueza()

@api_blueprint.route('/fraquezas/update', methods=['POST'])  
@token_required
def update_fraqueza():
    return update_controller_fraqueza()
#endregion

#region Especial
@api_blueprint.route('/especial/list', methods=['POST'])  
@token_required
def list_especiais():
    return especial_list()

@api_blueprint.route('/especial/listtype', methods=['POST'])  
@token_required
def list_especial_types():
    return especial_list_type()

@api_blueprint.route('/especial/new', methods=['POST'])  
@token_required
def save_especial():
    return save_controller_especial()

@api_blueprint.route('/especial/update', methods=['POST'])  
@token_required
def update_especial():
    return update_controller_especial()
#endregion

#region Elemento
@api_blueprint.route('/elemento/list', methods=['POST'])  
@token_required
def list_elementos():
    return elemento_list()

@api_blueprint.route('/elemento/new', methods=['POST'])  
@token_required
def save_elemento():
    return save_controller_elemento()

@api_blueprint.route('/elemento/update', methods=['POST'])  
@token_required
def update_elemento():
    return update_controller_elemento()
#endregion

#region Cria
@api_blueprint.route('/cria/list', methods=['POST'])  
@token_required
def list_crias():
    return busca_cria_com_relacoes()

@api_blueprint.route('/cria/new', methods=['POST'])  
@token_required
def save_cria():
    return save_controller_cria()

@api_blueprint.route('/cria/update', methods=['POST'])  
@token_required
def update_cria():
    return update_controller_cria()
#endregion

#region Chassi
@api_blueprint.route('/chassi/list', methods=['POST'])  
@token_required
def list_chassis():
    return chassi_list()

@api_blueprint.route('/chassi/new', methods=['POST'])  
@token_required
def save_chassi():
    return save_controller_chassi()

@api_blueprint.route('/chassi/update', methods=['POST'])  
@token_required
def update_chassi():
    return update_controller_chassi()
#endregion
