class Prestador():
    def __init__(self):
        self.__idprestador = 0
        self.__nome_empresa = ""
        self.__cidade = ""
        self.__uf = ""
        self.__cep = ""

        self._lista = 'nome_empresa, cidade, uf, cep'
        self.__dadosInserir = ""
        self.__dadosUpdate = ""
        self.__dadosDelete = ""
        self.__dadosPesquisa = ""
        self.__tabelaBanco = "prestador"

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self.__nome_empresa}', '{self.__cidade}', '{self.__uf}', '{self.__cep}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = (("nome_empresa='{}', cidade='{}', uf='{}', cep='{}' where idprestador='{}'")
                              .format(self.__nome_empresa, self.__cidade, self.__uf, self.__cep, self.__idprestador))
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idprestador='{}'".format(self.__idprestador)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from prestador where idprestador='{}'".format(self.__idprestador)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def lista(self):
        return self._lista

    @property
    def idprestador(self):
        return self.__idprestador

    @idprestador.setter
    def idprestador(self, value):
        self.__idprestador = value

    @property
    def nome_empresa(self):
        return self.__nome_empresa

    @nome_empresa.setter
    def nome_empresa(self, value):
        self.__nome_empresa = value

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, value):
        self.__cidade = value

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, value):
        self.__uf = value

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, value):
        self.__cep = value

    def __str__(self):
        return f"Prestador(idprestador={self.__idprestador}, nome_empresa='{self.__nome_empresa}', cidade='{self.__cidade}', uf='{self.__uf}', cep='{self.__cep}')"

    def __repr__(self):
        return self.__str__()

