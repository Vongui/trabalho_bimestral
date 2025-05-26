
class Cliente():
    def __init__(self):
        self._idcliente = 0
        self._nome = ""
        self._endereco = ""
        self._cidade = ""
        self._uf = ""
        self._cep = ""

        self._lista = 'nome, endereco, cidade, uf, cep'
        self.__dadosInserir = ""
        self.__dadosUpdate = ""
        self.__dadosDelete = ""
        self.__dadosPesquisa = ""
        self.__tabelaBanco = "cliente"

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self._nome}', '{self._endereco}', '{self._cidade}', '{self._uf}', '{self._cep}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = (("nome='{}',endereco='{}',cidade='{}',uf='{}',cep='{}' where idcliente='{}'")
                              .format(self._nome, self._endereco, self._cidade, self._uf, self._cep, self._idcliente))
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idcliente='{}'".format(self._idcliente)
        return self.__dadosDelete