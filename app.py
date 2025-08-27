from flask import Flask 
from db import db
from routes.Produtos_routes import Produtos_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Produtos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db.init_app(app)

app.register_blueprint(Produtos_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)