from flask import Blueprint, request
from controllers.Produtos_controllers import create_Produtos

Produtos_routes = Blueprint('Produtos_routes', __name__)

@Produtos_routes.route('/Produtos', methods=['POST'])
def Produtos_post():
    Produtos_data = request.json
    return create_Produtos(request.json)
    