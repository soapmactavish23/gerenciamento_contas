from flask_restful import Resource
from ..schemas import operacao_schema
from flask import request, make_response, jsonify
from ..entidades import operacao
from ..services import operacao_service
from app import api

class OperacaoList(Resource):
    def get(self):
        operacoes = operacao_service.listar_operacoes()
        os = operacao_schema.OperacaoSchema(many=True)
        return make_response(os.jsonify(operacoes), 200)
    def post(self):
        os = operacao_schema.OperacaoSchema()
        validate = os.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            custo = request.json["custo"]
            tipo = request.json["tipo"]

            operacao_nova = operacao.Operacao(
                nome=nome,
                resumo=resumo,
                custo=custo,
                tipo=tipo
            )
            resultado = operacao_service.cadastrar_operacao(operacao_nova)
            return make_response(os.jsonify(resultado), 201)

class OperacaoDetail(Resource):
    def get(self, id):
        operacao = operacao_service.listar_operacao_id(id)
        if operacao is None:
            return make_response(jsonify("Operação não encontrada"), 404)
        os = operacao_schema.OperacaoSchema()
        return make_response(os.jsonify(operacao), 200)

    def put(self, id):
        operacao_bd = operacao_service.listar_operacao_id(id)
        if operacao_bd is None:
            return make_response(jsonify("Operação Não encontrada"), 404)
        os = operacao_schema.OperacaoSchema()
        validate = os.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            custo = request.json["custo"]
            tipo = request.json["tipo"]
            operacao_nova = operacao.Operacao(
                nome=nome,
                resumo=resumo,
                custo=custo,
                tipo=tipo
            )
            resultado = operacao_service.atualizar_operacao(operacao_bd, operacao_nova)
            return make_response(os.jsonify(resultado), 200)


api.add_resource(OperacaoList, "/operacoes")
api.add_resource(OperacaoDetail, "/operacoes/<int:id>")