import traceback

from dao.connection import *
import json
import datetime

class ControllerGenerico:

    def __init__(self):
        self.ob = Banco()
        self.ob.configura(ho="localhost",
                          db="venda_trb",
                          us="root",
                          se="#Gm09191981",
                          po=3306)

    def incluir(self,objeto):
        self.ob.abrirConexao()
        sql = "insert into {} ".format(objeto.tabelaBanco)+'('
        sql+= '{}'.format(objeto.lista)
        sql+= ') values ({})'.format(objeto.dadosInserir)
        print(sql)

        try:
           self.ob.execute(sql)
           self.ob.gravar()
        except Exception as e:
           print(sql)
           print("Houve um erro", e)
           traceback.print_exc()
           self.ob.descarte()

    def alterar(self,objeto):
        self.ob.abrirConexao()
        sql = "update {} ".format(objeto.tabelaBanco)
        sql += 'set {}'.format(objeto.dadosUpdate)

        print(sql)
        try:
           self.ob.execute(sql)
           self.ob.gravar()
        except:
           print("Houve um erro")
           self.ob.descarte()


    def delete(self, objeto):
        self.ob.abrirConexao()
        sql = "delete from {} ".format(objeto.tabelaBanco)
        sql += objeto.dadosDelete

        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except Exception as e:
            print("Houve um erro", e)
            self.ob.descarte()

    def procuraRegistro(self,objeto):
        self.ob.abrirConexao()
        objeto = self.ob.selectQuery(objeto.dadosPesquisa)
        return objeto

    def listarTodos(self,objeto):
        self.ob.abrirConexao()
        dados = self.ob.selectQuery("select * from {}".format(objeto.tabelaBanco))
        return dados

