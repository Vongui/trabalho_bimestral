from flask import Flask, render_template, request, redirect, url_for, flash, json
import os

from controller.controller_cliente import ControllerCliente
from model.cliente import Cliente
from controller.controller_prestador import ControllerPrestador
from model.prestador import Prestador
from controller.controller_veiculo import ControllerVeiculo
from model.veiculo import Veiculo

controller_cliente = ControllerCliente()
controller_prestador = ControllerPrestador()
controller_veiculo = ControllerVeiculo()

app = Flask(__name__)
app.secret_key = '1234'

@app.route("/")
def index():
    return render_template("index.html", titulo="Página Inicial")



#==================================Cliente=====================================
@app.route("/listar-clientes")
def listar_clientes():
    clientes = controller_cliente.listarTodosRegistros(Cliente())
    print(clientes)
    return render_template("clientes/listar.html", titulo="Lista de Clientes", lista=clientes)

@app.route("/cadastrar-cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    if request.method == "POST":
        cliente = Cliente()

        cliente.nome = request.form["nome"]
        cliente.endereco = request.form["endereco"]
        cliente.cidade = request.form["cidade"]
        cliente.uf = request.form["uf"]
        cliente.cep = request.form["cep"]


        flash(f"Cliente {cliente.nome} cadastrado com sucesso!", "success")
        controller_cliente.incluir(cliente)

    return render_template("clientes/cadastrar.html", titulo="Cadastro de Clientes")

@app.route("/remover-cliente/<int:id>")
def remover_cliente(id):
    cliente = Cliente()

    cliente.idcliente = id
    controller_cliente.delete(cliente)
    flash("Cliente removido com sucesso!", "success")
    return redirect(url_for("listar_clientes"))

@app.route("/alterar-cliente/<int:id>", methods=["GET", "POST"])
def alterar_cliente(id):
    cliente = Cliente()
    cliente.idcliente = id

    if request.method == "POST":
        cliente.nome = request.form["nome"]
        cliente.endereco = request.form["endereco"]
        cliente.cidade = request.form["cidade"]
        cliente.uf = request.form["uf"]
        cliente.cep = request.form["cep"]

        controller_cliente.alterar(cliente)
        flash(f"Cliente {cliente.nome} alterado com sucesso!", "success")
        return redirect(url_for("listar_clientes"))

    cliente_dados = controller_cliente.pesquisaCodigo(cliente)
    return render_template("clientes/alterar.html", titulo="Alterar Cliente", cliente=cliente_dados)


#==================================Prestador=====================================
@app.route("/listar-prestadores")
def listar_prestadores():
    prestadores = controller_prestador.listarTodosRegistros(Prestador())
    return render_template("prestador/listar.html", titulo="Lista de Prestadores", lista=prestadores)

@app.route("/cadastrar-prestador", methods=["GET", "POST"])
def cadastrar_prestador():
    if request.method == "POST":
        prestador = Prestador()
        prestador.nome_empresa = request.form["nome_empresa"]
        prestador.cidade = request.form["cidade"]
        prestador.uf = request.form["uf"]
        prestador.cep = request.form["cep"]

        controller_prestador.incluir(prestador)

        flash(f"Prestador {prestador.nome_empresa} cadastrado com sucesso!", "success")
        return redirect(url_for("listar_prestadores"))

    return render_template("prestador/cadastrar.html", titulo="Cadastro de Prestadores")

@app.route("/remover-prestador/<int:id>")
def remover_prestador(id):
    prestador = Prestador()
    prestador.idprestador = id
    controller_prestador.delete(prestador)

    flash("Prestador removido com sucesso!", "success")
    return redirect(url_for("listar_prestadores"))

@app.route("/alterar-prestador/<int:id>", methods=["GET", "POST"])
def alterar_prestador(id):
    prestador = Prestador()
    prestador.idprestador = id

    if request.method == "POST":
        prestador.nome_empresa = request.form["nome_empresa"]
        prestador.cidade = request.form["cidade"]
        prestador.uf = request.form["uf"]
        prestador.cep = request.form["cep"]

        controller_prestador.alterar(prestador)
        flash(f"Prestador {prestador.nome_empresa} alterado com sucesso!", "success")
        return redirect(url_for("listar_prestadores"))

    prestador_dados = controller_prestador.pesquisaCodigo(prestador)
    return render_template("prestador/alterar.html", titulo="Alterar Prestador", prestador=prestador_dados)


#=========================== Veículo ==============================
@app.route("/listar-veiculos")
def listar_veiculos():
    veiculos = controller_veiculo.listarTodosRegistros(Veiculo())
    return render_template("veiculo/listar.html", titulo="Lista de Veículos", lista=veiculos)

@app.route("/cadastrar-veiculo", methods=["GET", "POST"])
def cadastrar_veiculo():
    if request.method == "POST":
        veiculo = Veiculo()

        veiculo.idplaca = request.form["idplaca"]
        veiculo.ano = int(request.form["ano"])
        veiculo.modelo = int(request.form["modelo"])
        veiculo.preco_fipe = float(request.form["preco_fipe"])
        veiculo.fabricante = request.form["fabricante"]
        veiculo.modelo_veiculo = request.form["modelo_veiculo"]
        veiculo.cor = request.form["cor"]

        controller_veiculo.incluir(veiculo)
        flash(f"Veículo {veiculo.idplaca} cadastrado com sucesso!", "success")
        return redirect(url_for("listar_veiculos"))

    return render_template("veiculo/cadastrar.html", titulo="Cadastro de Veículo")

@app.route("/remover-veiculo/<string:idplaca>")
def remover_veiculo(idplaca):
    veiculo = Veiculo()
    veiculo.idplaca = idplaca
    controller_veiculo.delete(veiculo)
    flash("Veículo removido com sucesso!", "success")
    return redirect(url_for("listar_veiculos"))

@app.route("/alterar-veiculo/<string:idplaca>", methods=["GET", "POST"])
def alterar_veiculo(idplaca):
    veiculo = Veiculo()
    veiculo.idplaca = idplaca

    if request.method == "POST":
        veiculo.ano = int(request.form["ano"])
        veiculo.modelo = int(request.form["modelo"])
        veiculo.preco_fipe = float(request.form["preco_fipe"])
        veiculo.fabricante = request.form["fabricante"]
        veiculo.modelo_veiculo = request.form["modelo_veiculo"]
        veiculo.cor = request.form["cor"]
        veiculo.preco_venda = float(request.form["preco_venda"])
        veiculo.total_despesa = float(request.form["total_despesa"])

        controller_veiculo.alterar(veiculo)
        flash(f"Veículo {veiculo.idplaca} alterado com sucesso!", "success")
        return redirect(url_for("listar_veiculos"))

    veiculo_dados = controller_veiculo.pesquisaCodigo(veiculo)
    return render_template("veiculo/alterar.html", titulo="Alterar Veículo", veiculo=veiculo_dados)




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
