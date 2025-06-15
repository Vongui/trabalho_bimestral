from controller.controller_generico import ControllerGenerico
from model.compra import Compra

class ControllerCompra(ControllerGenerico):

    def incluir_compra(self, compra):
        self.incluir(compra)

    def delete_compra(self, compra):
        self.delete(compra)

    def alterar_compra(self, compra):
        self.alterar(compra)

    def pesquisaCodigo(self, entrada):
        compra_obj = Compra()
        compra_obj.idcompra = entrada
        compra = self.procuraRegistro(compra_obj)
        if len(compra) >= 1:
            retorno = self.converte_compra(compra)
        return retorno

    def converte_compra(self, compra):
        retorno = Compra()
        retorno.idcompra = compra[0][0]
        retorno.idplaca = compra[0][1]
        retorno.idcliente = compra[0][2]
        retorno.data = compra[0][3]
        retorno.valor_pago = compra[0][4]
        retorno.forma_pagamento = compra[0][5]
        return retorno

    def converte_objeto(self, entrada):
        compra = Compra()
        compra.idcompra = entrada[0]
        compra.idplaca = entrada[1]
        compra.idcliente = entrada[2]
        compra.data = entrada[3]
        compra.valor_pago = entrada[4]
        compra.forma_pagamento = entrada[5]
        return compra

    def listarTodosRegistros(self, objeto):
        registros = self.listarTodos(objeto)
        compras = []
        for registro in registros:
            compras.append(self.converte_objeto(registro))
        return compras

    def dadosJson(self, dados):
        return {
            "idcompra": dados.idcompra,
            "data": dados.data,
            "idveiculo": dados.idveiculo,
            "valor_pago": dados.valor_pago,
            "total_despesas": dados.total_despesas,
            "forma_pagamento": dados.forma_pagamento
        }
