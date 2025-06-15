class Compra:
    def __init__(self):
        self.__idcompra = 0
        self.__idplaca = ""
        self.__idcliente = 0
        self.__data = ""
        self.__valor_pago = 0.0
        self.__forma_pagamento = ""

        self.__tabelaBanco = "compra"
        self.__lista = "idplaca, idcliente, data, valor_pago, forma_pagamento"
        self.__dadosInserir = ""
        self.__dadosDelete = ""
        self.__dadosUpdate = ""
        self.__dadosPesquisa = ""

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self.__idplaca}', {self.__idcliente}, '{self.__data}', {self.__valor_pago}, '{self.__forma_pagamento}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = ("idplaca='{}', idcliente={}, data='{}', valor_pago={}, forma_pagamento='{}' where idcompra={}").format(
            self.__idplaca, self.__idcliente, self.__data, self.__valor_pago, self.__forma_pagamento, self.__idcompra)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = f"where idcompra={self.__idcompra}"
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = f"select * from compra where idcompra={self.__idcompra}"
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def lista(self):
        return self.__lista

    # Getters e setters
    @property
    def idcompra(self):
        return self.__idcompra

    @idcompra.setter
    def idcompra(self, value):
        self.__idcompra = value

    @property
    def idplaca(self):
        return self.__idplaca

    @idplaca.setter
    def idplaca(self, value):
        self.__idplaca = value

    @property
    def idcliente(self):
        return self.__idcliente

    @idcliente.setter
    def idcliente(self, value):
        self.__idcliente = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, value):
        self.__valor_pago = value

    @property
    def forma_pagamento(self):
        return self.__forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, value):
        self.__forma_pagamento = value

    def __str__(self):
        return f"Compra(idcompra={self.__idcompra}, idplaca='{self.__idplaca}', idcliente={self.__idcliente}, data='{self.__data}', valor_pago={self.__valor_pago}, forma_pagamento='{self.__forma_pagamento}')"

    def __repr__(self):
        return self.__str__()