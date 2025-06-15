class Despesa:
    def __init__(self):
        self.__iddespesa = 0
        self.__idplaca = ""
        self.__idprestador = 0
        self.__descricao = ""
        self.__data_servico = ""
        self.__valor = 0.0

        self._lista = 'iddespesa, idplaca, idprestador, descricao, data_servico, valor'
        self.__dadosInserir = ""
        self.__dadosDelete = ""
        self.__dadosUpdate = ""
        self.__dadosPesquisa = ""
        self.__tabelaBanco = "despesa"

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"{self.__iddespesa}, '{self.__idplaca}',{self.__idprestador},'{self.__descricao}','{self.__data_servico}',{self.__valor}"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = ("idprestador={},descricao='{}',data_servico='{}',valor={} where iddespesa={}").format(
            self.__idprestador, self.__descricao, self.__data_servico, self.__valor, self.__iddespesa)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where iddespesa={}".format(self.__iddespesa)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from despesa where iddespesa={}".format(self.__iddespesa)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def lista(self):
        return self._lista

    @property
    def iddespesa(self):
        return self.__iddespesa

    @property
    def idplaca(self):
        return self.__idplaca

    @property
    def idprestador(self):
        return self.__idprestador

    @property
    def descricao(self):
        return self.__descricao

    @property
    def data_servico(self):
        return self.__data_servico

    @property
    def valor(self):
        return self.__valor

    @iddespesa.setter
    def iddespesa(self, value):
        self.__iddespesa = value

    @idplaca.setter
    def idplaca(self, value):
        self.__idplaca = value

    @idprestador.setter
    def idprestador(self, value):
        self.__idprestador = value

    @descricao.setter
    def descricao(self, value):
        self.__descricao = value

    @data_servico.setter
    def data_servico(self, value):
        self.__data_servico = value

    @valor.setter
    def valor(self, value):
        self.__valor = value

    def __str__(self):
        return f"Despesa(id={self.__iddespesa}, placa={self.__idplaca}, prestador={self.__idprestador}, descricao='{self.__descricao}', data_servico='{self.__data_servico}', valor={self.__valor})"

    def __repr__(self):
        return self.__str__()
