from app import db
from ..models import conta_model

def listar_contas():
    contas = conta_model.Conta.query.all()
    return contas

def listar_conta_id(id):
    conta = conta_model.Conta.query.filter_by(id=id).first()
    return conta

def cadastrar_conta(conta):
    conta_bd = conta_model.Conta(nome=conta.nome, resumo=conta.resumo, valor=conta.valor)
    db.session.add(conta_bd)
    db.session.commit()
    return conta_bd
