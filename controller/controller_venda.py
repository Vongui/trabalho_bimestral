from controller.controller_generico import ControllerGenerico
from model.venda import Venda

class ControllerVenda(ControllerGenerico):

    def incluir_venda(self, venda):
        self.incluir(venda)

    def delete_venda(self, venda):
        self.delete(venda)

    def alterar_venda(self, venda):
        self.alterar(venda)

    def pesquisaCodigo(self, entrada):
        venda_obj = Venda()
        venda_obj.idvenda = entrada
        venda = self.procuraRegistro(venda_obj)
        retorno = None
        if len(venda) >= 1:
            retorno = self.converte_venda(venda)
        return retorno

    def converte_venda(self, venda):
        retorno = Venda()
        retorno.idvenda = venda[0][0]
        retorno.idcliente = venda[0][1]
        retorno.idplaca = venda[0][2]
        retorno.data = venda[0][3]
        retorno.valor_vendido = venda[0][4]
        retorno.forma_pagamento = venda[0][5]
        return retorno

    def converte_objeto(self, entrada):
        venda = Venda()
        venda.idvenda = entrada[0]
        venda.idcliente = entrada[1]
        venda.idplaca = entrada[2]
        venda.data = entrada[3]
        venda.valor_vendido = entrada[4]
        venda.forma_pagamento = entrada[5]
        return venda

    def listarTodosRegistros(self, objeto):
        registros = self.listarTodos(objeto)
        vendas = []
        for registro in registros:
            vendas.append(self.converte_objeto(registro))
        return vendas

    def dadosJson(self, dados):
        return {
            "idvenda": dados.idvenda,
            "data": dados.data,
            "idplaca": dados.idplaca,
            "valor_vendido": dados.valor_vendido,
            "idcliente": dados.idcliente,
            "forma_pagamento": dados.forma_pagamento
        }
