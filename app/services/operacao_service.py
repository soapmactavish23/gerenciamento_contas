from app import db
from ..models import operacao_model

def listar_operacoes():
    operacoes = operacao_model.Operacao.query.all()
    return operacoes

def cadastrar_operacao(operacao):
    operacao_bd = operacao_model.Operacao(
        nome=operacao.nome,
        resumo=operacao.resumo,
        custo=operacao.custo,
        tipo=operacao.tipo
    )
    db.session.add(operacao_bd)
    db.session.commit()
    return operacao_bd