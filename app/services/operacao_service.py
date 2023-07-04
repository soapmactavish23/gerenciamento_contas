from app import db
from ..models import operacao_model

def listar_operacoes():
    operacoes = operacao_model.Operacao.query.all()
    return operacoes

def listar_operacao_id(id):
    operacao = operacao_model.Operacao.query.filter_by(id=id).first()
    return operacao

def cadastrar_operacao(operacao):
    operacao_bd = operacao_model.Operacao(
        nome=operacao.nome,
        resumo=operacao.resumo,
        custo=operacao.custo,
        tipo=operacao.tipo,
        conta_id=operacao.conta
    )
    db.session.add(operacao_bd)
    db.session.commit()
    return operacao_bd

def atualizar_operacao(operacao, operacao_nova):
    operacao.nome = operacao_nova.nome
    operacao.resumo = operacao_nova.resumo
    operacao.custo = operacao_nova.custo
    operacao.tipo = operacao_nova.tipo
    operacao.conta = operacao_nova.conta

    db.session.commit()
    return operacao

def exclui_operacao(operacao):
    db.session.delete(operacao)
    db.session.commit()