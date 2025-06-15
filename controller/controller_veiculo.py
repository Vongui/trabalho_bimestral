from controller.controller_generico import ControllerGenerico
from model.veiculo import Veiculo

class ControllerVeiculo(ControllerGenerico):

    def incluir_veiculo(self, veiculo):
        self.incluir(veiculo)

    def delete_veiculo(self, veiculo):
        self.delete(veiculo)

    def alterar_veiculo(self, veiculo):
        self.alterar(veiculo)

    def pesquisaCodigo(self, entrada):
        veiculo = self.procuraRegistro(entrada)
        retorno = None
        if len(veiculo) >= 1:
            retorno = self.converte_veiculo(veiculo)
        return retorno

    def converte_veiculo(self, veiculo):
        retorno = Veiculo()
        retorno.idplaca = veiculo[0][0]
        retorno.ano = veiculo[0][1]
        retorno.modelo = veiculo[0][2]
        retorno.preco_fipe = veiculo[0][3]
        retorno.fabricante = veiculo[0][4]
        retorno.modelo_veiculo = veiculo[0][5]
        retorno.cor = veiculo[0][6]
        retorno.preco_venda = veiculo[0][7]
        retorno.total_despesa = veiculo[0][8]
        retorno.status = veiculo[0][9]  # NOVO
        return retorno

    def converte_objeto(self, entrada):
        veiculo = Veiculo()
        veiculo.idplaca = entrada[0]
        veiculo.ano = entrada[1]
        veiculo.modelo = entrada[2]
        veiculo.preco_fipe = entrada[3]
        veiculo.fabricante = entrada[4]
        veiculo.modelo_veiculo = entrada[5]
        veiculo.cor = entrada[6]
        veiculo.preco_venda = entrada[7]
        veiculo.total_despesa = entrada[8]
        veiculo.status = entrada[9]  # NOVO
        return veiculo

    def listarTodosRegistros(self, objeto):
        registros = self.listarTodos(objeto)
        veiculos = []
        for registro in registros:
            veiculo = self.converte_objeto(registro)
            veiculos.append(veiculo)
        return veiculos

    def dadosJson(self, dados):
        retorno = {}

        retorno["idplaca"] = dados.idplaca
        retorno["ano"] = dados.ano
        retorno["modelo"] = dados.modelo
        retorno["preco_fipe"] = dados.preco_fipe
        retorno["fabricante"] = dados.fabricante
        retorno["modelo_veiculo"] = dados.modelo_veiculo
        retorno["cor"] = dados.cor
        retorno["preco_venda"] = dados.preco_venda
        retorno["total_despesa"] = dados.total_despesa
        retorno["status"] = dados.status
        return retorno

