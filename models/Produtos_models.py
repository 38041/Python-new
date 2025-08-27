from db import db

class Produtos(db.Model):
    __tablename__ = 'Produtos'

    id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(80), nullable=False)
    Categoria = db.Column(db.String(80), nullable=False)
    Preço= db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'Nome': self.Nome,
            'Categoria': self.Categoria,
            'Preço': self.Preço
        }