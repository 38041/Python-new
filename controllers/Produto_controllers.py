from models.Produtos_models import Produtos
from db import db
import json
from flask import make_response

def create_Produtos(Produtos_data):
    novo_Produtos = Produtos(
        Nome=Produtos_data['Nome'],
        Categoria=Produtos_data['Categoria'],
        Preço=Produtos_data['Preço']
    )
    db.session.add(novo_Produtos)
    db.session.commit()
    response = make_response(
        json.dumps({
            'mensagem': 'Produtos cadastrado com secusso',
            'Produtos': novo_Produtos.json()
        }, sort_keys=False)
    )
    response.headers['content-Type'] = 'application/json'
    return response