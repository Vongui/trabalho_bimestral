from controller.controller_generico import ControllerGenerico
from model.prestador import Prestador

class ControllerPrestador(ControllerGenerico):

    def incluir_prestador(self, prestador):
        self.incluir(prestador)

    def delete_prestador(self, prestador):
        self.delete(prestador)

    def alterar_prestador(self, prestador):
        self.alterar(prestador)

    def pesquisaCodigo(self, entrada):
        prestador = self.procuraRegistro(entrada)
        retorno = None
        if len(prestador) >= 1:
            retorno = self.converte_prestador(prestador)
        return retorno

    def converte_prestador(self, prestador):
        retorno = Prestador()

        retorno.idprestador = prestador[0][0]
        retorno.nome_empresa = prestador[0][1]
        retorno.cidade = prestador[0][2]
        retorno.uf = prestador[0][3]
        retorno.cep = prestador[0][4]

        return retorno

    def converte_objeto(self, entrada):
        prestador = Prestador()

        prestador.idprestador = entrada[0]
        prestador.nome_empresa = entrada[1]
        prestador.cidade = entrada[2]
        prestador.uf = entrada[3]
        prestador.cep = entrada[4]

        return prestador

    def listarTodosRegistros(self, objeto):
        registros = self.listarTodos(objeto)
        prestadores = []
        for registro in registros:
            prestador = self.converte_objeto(registro)
            prestadores.append(prestador)
        return prestadores

    def dadosJson(self, dados):
        retorno = {}

        retorno["idprestador"] = dados.idprestador
        retorno["nome_empresa"] = dados.nome_empresa
        retorno["cidade"] = dados.cidade
        retorno["uf"] = dados.uf
        retorno["cep"] = dados.cep

        return retorno

