
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

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from cliente where idcliente='{}'".format(self._idcliente)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def lista(self):
        return self._lista

    @property
    def idcliente(self):
        return self._idcliente

    @idcliente.setter
    def idcliente(self, value):
        self._idcliente = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value):
        self._endereco = value

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, value):
        self._cidade = value

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, value):
        self._uf = value

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, value):
        self._cep = value

    def __str__(self):
        return (f"Cliente(idcliente={self._idcliente}, nome='{self._nome}', "
                f"endereco='{self._endereco}', cidade='{self._cidade}', "
                f"uf='{self._uf}', cep='{self._cep}')")

    def __repr__(self):
        return self.__str__()
