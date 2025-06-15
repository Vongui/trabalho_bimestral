from controller.controller_generico import ControllerGenerico
from model.despesa import Despesa

class ControllerDespesa(ControllerGenerico):
    def incluir_despesa(self, despesa):
        self.incluir(despesa)

    def delete_despesa(self, despesa):
        self.delete(despesa)

    def alterar_despesa(self, despesa):
        self.alterar(despesa)

    def pesquisaCodigo(self, iddespesa):
        despesa_obj = Despesa()
        despesa_obj.iddespesa = iddespesa
        registros = self.procuraRegistro(despesa_obj)
        if registros and len(registros) >= 1:
            return self.converte_despesa(registros[0])
        else:
            return None

    def converte_despesa(self, despesa):
        retorno = Despesa()
        retorno.iddespesa = despesa[0]
        retorno.idplaca = despesa[1]
        retorno.descricao = despesa[2]
        retorno.idprestador = despesa[3]
        retorno.data_servico = despesa[4]
        retorno.valor = despesa[5]
        return retorno

    def converte_objeto(self, entrada):
        despesa = Despesa()
        despesa.iddespesa = entrada[0]
        despesa.idplaca = entrada[1]
        despesa.descricao = entrada[2]
        despesa.idprestador = entrada[3]
        despesa.data_servico = entrada[4]
        despesa.valor = entrada[5]
        return despesa

    def listarTodosRegistros(self, objeto):
        registros = self.listarTodos(objeto)
        despesas = []
        for registro in registros:
            despesa = self.converte_objeto(registro)
            despesas.append(despesa)
        return despesas

    def dadosJson(self, dados):
        retorno = {}
        retorno["iddespesa"] = dados.iddespesa
        retorno["idplaca"] = dados.idplaca
        retorno["idprestador"] = dados.idprestador
        retorno["descricao"] = dados.descricao
        retorno["data_servico"] = dados.data_servico
        retorno["valor"] = dados.valor
        return retorno

    def listarDespesasPorPlaca(self, idplaca):
        despesas = self.listarTodosRegistros(Despesa())
        despesas_filtradas = [d for d in despesas if d.idplaca == idplaca]
        return despesas_filtradas

    def listarDespesasPorPrestador(self, idprestador):
        despesas = self.listarTodosRegistros(Despesa())
        despesas_filtradas = [d for d in despesas if d.idprestador == idprestador]
        return despesas_filtradas

    def obter_proximo_id(self):
        self.ob.abrirConexao()
        sql = "SELECT MAX(iddespesa) FROM despesa"
        try:
            resultado = self.ob.selectQuery(sql)
            ultimo_id = resultado[0][0] if resultado and resultado[0][0] is not None else 0
            return ultimo_id + 1
        except Exception as e:
            print("Erro ao obter próximo ID:", e)
            return 1


