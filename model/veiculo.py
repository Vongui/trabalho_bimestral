class Veiculo:
    def __init__(self):
        self.__idplaca = ""
        self.__ano = ""
        self.__modelo = ""
        self.__preco_fipe = 0.0
        self.__fabricante = ""
        self.__modelo_veiculo = ""
        self.__cor = ""
        self.__preco_venda = 0.0
        self.__total_despesa = 0.0
        self.__status = 0 #0 = na loja, 1 = vendido, 2 = comprado

        self.__lista = 'idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa, status'
        self.__dadosInserir = ""
        self.__dadosDelete = ""
        self.__dadosUpdate = ""
        self.__dadosPesquisa = ""
        self.__tabelaBanco = "veiculo"


    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self.__idplaca}', '{self.__ano}', '{self.__modelo}', {self.__preco_fipe}, '{self.__fabricante}', '{self.__modelo_veiculo}', '{self.__cor}', {self.__preco_venda}, {self.__total_despesa}, {self.__status}"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = ("idplaca='{}', ano='{}', modelo='{}', preco_fipe={}, fabricante='{}', modelo_veiculo='{}', cor='{}', preco_venda={}, total_despesa={}, status={} where idplaca='{}'").format(
            self.__idplaca, self.__ano, self.__modelo, self.__preco_fipe, self.__fabricante, self.__modelo_veiculo, self.__cor, self.__preco_venda, self.__total_despesa, self.__status ,self.__idplaca)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idplaca='{}'".format(self.__idplaca)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from veiculo where idplaca='{}'".format(self.__idplaca)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def lista(self):
        return self.__lista

    @property
    def idplaca(self):
        return self.__idplaca

    @property
    def ano(self):
        return self.__ano

    @property
    def modelo(self):
        return self.__modelo

    @property
    def preco_fipe(self):
        return self.__preco_fipe

    @property
    def fabricante(self):
        return self.__fabricante

    @property
    def modelo_veiculo(self):
        return self.__modelo_veiculo

    @property
    def cor(self):
        return self.__cor

    @property
    def preco_venda(self):
        return self.__preco_venda

    @property
    def total_despesa(self):
        return self.__total_despesa

    @idplaca.setter
    def idplaca(self, value):
        self.__idplaca = value

    @ano.setter
    def ano(self, value):
        self.__ano = value

    @modelo.setter
    def modelo(self, value):
        self.__modelo = value

    @preco_fipe.setter
    def preco_fipe(self, value):
        self.__preco_fipe = value

    @fabricante.setter
    def fabricante(self, value):
        self.__fabricante = value

    @modelo_veiculo.setter
    def modelo_veiculo(self, value):
        self.__modelo_veiculo = value

    @cor.setter
    def cor(self, value):
        self.__cor = value

    @preco_venda.setter
    def preco_venda(self, value):
        self.__preco_venda = value

    @total_despesa.setter
    def total_despesa(self, value):
        self.__total_despesa = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def __str__(self):
        return f"Veiculo(idplaca={self.__idplaca}, ano={self.__ano}, modelo={self.__modelo}, preco_fipe={self.__preco_fipe}, fabricante={self.__fabricante}, modelo_veiculo={self.__modelo_veiculo}, cor={self.__cor}, preco_venda={self.__preco_venda}, total_despesa={self.__total_despesa})"

    def __repr__(self):
        return self.__str__()

