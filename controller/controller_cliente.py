from controller.controller_generico import ControllerGenerico
from model.cliente import Cliente


class ControllerCliente(ControllerGenerico):

    def incluir_cliente(self, cliente_data):
        return self.incluir(cliente_data)

    def alterar_cliente(self, cliente_data):
        return self.alterar(cliente_data)

    def delete_cliente(self, cliente_id):
        return self.delete(cliente_id)

    def pesquisaCodigo(self, entrada):
        cliente = self.procuraRegistro(entrada)
        retorno = Cliente()
        if len(cliente) >= 1:
            retorno = self.converte_cliente(cliente)
        return retorno

    def converte_cliente(self, cliente):
        retorno = Cliente()

        retorno.idcliente = cliente[0][0]
        retorno.nome = cliente[0][1]
        retorno.endereco = cliente[0][2]
        retorno.cidade = cliente[0][3]
        retorno.uf = cliente[0][4]
        retorno.cep = cliente[0][5]
        return retorno

    def converte_objeto(self, entrada):
        cliente = Cliente()

        cliente.idcliente = entrada[0]
        cliente.nome = entrada[1]
        cliente.endereco = entrada[2]
        cliente.cidade = entrada[3]
        cliente.uf = entrada[4]
        cliente.cep = entrada[5]
        return cliente

    def listarTodosRegistros(self, objeto):
        registros = self.listarTodos(objeto)
        clientes = []
        for registro in registros:
            cliente = self.converte_objeto(registro)
            clientes.append(cliente)
        return clientes

    def dadosJson(self, dados):
        retorno = {}

        retorno["idcliente"] = dados.idcliente
        retorno["nome"] = dados.nome
        retorno["endereco"] = dados.endereco
        retorno["cidade"] = dados.cidade
        retorno["uf"] = dados.uf
        retorno["cep"] = dados.cep
        return retorno

