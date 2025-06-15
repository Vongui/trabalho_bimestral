class Venda:
    def __init__(self):
        self.__idvenda = 0
        self.__idcliente = 0
        self.__idplaca = ""
        self.__data = ""
        self.__valor_vendido = 0.0
        self.__forma_pagamento = ""

        self.__tabelaBanco = "venda"
        self.__lista = "idcliente, idplaca, data, valor_vendido, forma_pagamento"
        self.__dadosInserir = ""
        self.__dadosDelete = ""
        self.__dadosUpdate = ""
        self.__dadosPesquisa = ""

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"{self.__idcliente}, '{self.__idplaca}', '{self.__data}', {self.__valor_vendido}, '{self.__forma_pagamento}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = ("idcliente={}, idplaca='{}', data='{}', valor_vendido={}, forma_pagamento='{}' where idvenda={}").format(
            self.__idcliente, self.__idplaca, self.__data, self.__valor_vendido, self.__forma_pagamento, self.__idvenda)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = f"where idvenda={self.__idvenda}"
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = f"select * from venda where idvenda={self.__idvenda}"
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def lista(self):
        return self.__lista

    # Getters e setters
    @property
    def idvenda(self):
        return self.__idvenda

    @idvenda.setter
    def idvenda(self, value):
        self.__idvenda = value

    @property
    def idcliente(self):
        return self.__idcliente

    @idcliente.setter
    def idcliente(self, value):
        self.__idcliente = value

    @property
    def idplaca(self):
        return self.__idplaca

    @idplaca.setter
    def idplaca(self, value):
        self.__idplaca = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def valor_vendido(self):
        return self.__valor_vendido

    @valor_vendido.setter
    def valor_vendido(self, value):
        self.__valor_vendido = value

    @property
    def forma_pagamento(self):
        return self.__forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, value):
        self.__forma_pagamento = value

    def __str__(self):
        return f"Venda(idvenda={self.__idvenda}, idcliente={self.__idcliente}, idplaca='{self.__idplaca}', data='{self.__data}', valor_vendido={self.__valor_vendido}, forma_pagamento='{self.__forma_pagamento}')"

    def __repr__(self):
        return self.__str__()