from app import db
from ..models import conta_model

def cadastrar_conta(conta):
    conta_bd = conta_model.Conta(nome=conta.nome, resumo=conta.resumo, valor=conta.valor)
    db.session.add(conta_bd)
    db.session.commit()
    return conta_bd
