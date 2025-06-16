from flask import Flask, render_template, request, redirect, url_for, flash, json
import os

from controller.controller_cliente import ControllerCliente
from model.cliente import Cliente
from controller.controller_prestador import ControllerPrestador
from model.prestador import Prestador
from controller.controller_veiculo import ControllerVeiculo
from model.veiculo import Veiculo
from controller.controller_despesa import ControllerDespesa
from model.despesa import Despesa
from controller.controller_compra import ControllerCompra
from model.compra import Compra
from controller.controller_venda import ControllerVenda
from model.venda import Venda

controller_cliente = ControllerCliente()
controller_prestador = ControllerPrestador()
controller_veiculo = ControllerVeiculo()
controller_despesa = ControllerDespesa()
controller_compra = ControllerCompra()
controller_venda = ControllerVenda()

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
        return redirect(url_for("listar_clientes"))

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
    return render_template("clientes/editar.html", titulo="Alterar Cliente", cliente=cliente_dados)


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
    return render_template("prestador/editar.html", titulo="Alterar Prestador", prestador=prestador_dados)


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
        veiculo.preco_venda = float(request.form["preco_venda"])

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
    return render_template("veiculo/editar.html", titulo="Alterar Veículo", veiculo=veiculo_dados)

# ========================== DESPESA ===============================

@app.route("/listar-despesas")
def listar_despesas():
    despesas = controller_despesa.listarTodosRegistros(Despesa())
    return render_template("despesa/listar.html", titulo="Lista de Despesas", lista=despesas)

@app.route("/cadastrar-despesa", methods=["GET", "POST"])
def cadastrar_despesa():
    veiculos = controller_veiculo.listarTodosRegistros(Veiculo())
    prestadores = controller_prestador.listarTodosRegistros(Prestador())

    if not veiculos or not prestadores:
        flash("Não é possível cadastrar despesa porque não há veículos ou prestadores cadastrados.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        despesa = Despesa()
        despesa.iddespesa = controller_despesa.obter_proximo_id()
        despesa.idplaca = request.form["idplaca"]
        despesa.idprestador = int(request.form["idprestador"])
        despesa.descricao = request.form["descricao"]
        despesa.data_servico = request.form["data_servico"]
        despesa.valor = float(request.form["valor"])

        controller_despesa.incluir_despesa(despesa)
        flash("Despesa cadastrada com sucesso!", "success")
        return redirect(url_for("listar_despesas"))

    idplaca_selecionada = request.args.get("idplaca")

    return render_template("despesa/cadastrar.html", titulo="Cadastro de Despesa", veiculos=veiculos, prestadores=prestadores,idplaca=idplaca_selecionada)

@app.route("/remover-despesa/<int:iddespesa>")
def remover_despesa(iddespesa):
    despesa = Despesa()
    despesa.iddespesa = iddespesa
    controller_despesa.delete_despesa(despesa)
    flash("Despesa removida com sucesso!", "success")
    return redirect(url_for("listar_despesas"))

@app.route("/alterar-despesa/<int:iddespesa>", methods=["GET", "POST"])
def alterar_despesa(iddespesa):
    veiculos = controller_veiculo.listarTodosRegistros(Veiculo())
    prestadores = controller_prestador.listarTodosRegistros(Prestador())

    if request.method == "POST":
        despesa = Despesa()
        despesa.iddespesa = iddespesa
        despesa.idplaca = request.form["idplaca"]
        despesa.idprestador = int(request.form["idprestador"])
        despesa.descricao = request.form["descricao"]
        despesa.data_servico = request.form["data_servico"]
        despesa.valor = float(request.form["valor"])

        controller_despesa.alterar_despesa(despesa)
        flash("Despesa alterada com sucesso!", "success")
        return redirect(url_for("listar_despesas"))

    despesa_dados = controller_despesa.pesquisaCodigo(iddespesa)
    if despesa_dados is None:
        flash("Despesa não encontrada.", "error")
        return redirect(url_for("listar_despesas"))

    return render_template(
        "despesa/editar.html",titulo="Alterar Despesa",despesa=despesa_dados,veiculos=veiculos,prestadores=prestadores,)


# ========================== COMPRA ===============================

@app.route("/listar-compras")
def listar_compras():
    compras = controller_compra.listarTodosRegistros(Compra())
    print(compras)
    return render_template("compra/listar.html", titulo="Lista de Compras", lista=compras)

@app.route("/cadastrar-compra", methods=["GET", "POST"])
def cadastrar_compra():
    veiculos = controller_veiculo.listarTodosRegistros(Veiculo())
    clientes = controller_cliente.listarTodosRegistros(Cliente())

    if request.method == "POST":
        compra = Compra()
        compra.idplaca = request.form["idplaca"]
        compra.idcliente = int(request.form["idcliente"])
        compra.data = request.form["data_compra"]
        compra.valor_pago = float(request.form["valor"])
        compra.forma_pagamento = request.form["forma_pagamento"]

        controller_compra.incluir_compra(compra)
        flash("Compra cadastrada com sucesso!", "success")
        for v in veiculos:
            if v.idplaca == compra.idplaca:
                v.status = 2
                controller_veiculo.alterar(v)
                break

        return redirect(url_for("listar_compras"))

    return render_template("compra/cadastrar.html", titulo="Cadastro de Compra", veiculos=veiculos, clientes=clientes)


@app.route("/remover-compra/<int:idcompra>")
def remover_compra(idcompra):
    compra = Compra()
    compra.idcompra = idcompra
    controller_compra.delete_compra(compra)
    flash("Compra removida com sucesso!", "success")
    return redirect(url_for("listar_compras"))

@app.route("/alterar-compra/<int:idcompra>", methods=["GET", "POST"])
def alterar_compra(idcompra):
    veiculos = controller_veiculo.listarTodosRegistros(Veiculo())
    clientes = controller_cliente.listarTodosRegistros(Cliente())

    if request.method == "POST":
        compra = Compra()
        compra.idcompra = idcompra
        compra.idplaca = request.form["idplaca"]
        compra.idcliente = int(request.form["idcliente"])
        compra.data = request.form["data"]
        compra.valor_pago = float(request.form["valor_pago"])
        compra.forma_pagamento = request.form["forma_pagamento"]

        controller_compra.alterar_compra(compra)
        flash("Compra alterada com sucesso!", "success")
        return redirect(url_for("listar_compras"))

    compra_dados = controller_compra.pesquisaCodigo(idcompra)
    return render_template("compra/editar.html", titulo="Alterar Compra", compra=compra_dados, veiculos=veiculos, clientes=clientes)

# ========================== VENDA ===============================
@app.route("/listar-vendas")
def listar_vendas():
    vendas = controller_venda.listarTodosRegistros(Venda())
    print(vendas)
    return render_template("venda/listar.html", titulo="Lista de Vendas", lista=vendas)

@app.route("/cadastrar-venda", methods=["GET", "POST"])
def cadastrar_venda():
    veiculos = controller_veiculo.listarTodosRegistros(Veiculo())
    clientes = controller_cliente.listarTodosRegistros(Cliente())

    if request.method == "POST":
        venda = Venda()
        venda.idplaca = request.form["idplaca"]
        venda.idcliente = int(request.form["idcliente"])
        venda.data = request.form["data_venda"]
        venda.valor_vendido = float(request.form["valor_vendido"])
        venda.forma_pagamento = request.form["forma_pagamento"]

        controller_venda.incluir_venda(venda)
        flash("Venda cadastrada com sucesso!", "success")
        for v in veiculos:
            if v.idplaca == venda.idplaca:
                v.status = 1
                controller_veiculo.alterar(v)
                break

        return redirect(url_for("listar_vendas"))

    return render_template("venda/cadastrar.html", titulo="Cadastro de Venda", veiculos=veiculos, clientes=clientes)

@app.route("/remover-venda/<int:idvenda>")
def remover_venda(idvenda):
    venda = Venda()
    venda.idvenda = idvenda
    controller_venda.delete_venda(venda)
    flash("Venda removida com sucesso!", "success")
    return redirect(url_for("listar_vendas"))

@app.route("/alterar-venda/<int:idvenda>", methods=["GET", "POST"])
def alterar_venda(idvenda):
    veiculos = controller_veiculo.listarTodosRegistros(Veiculo())
    clientes = controller_cliente.listarTodosRegistros(Cliente())

    if request.method == "POST":
        venda = Venda()
        venda.idvenda = idvenda
        venda.idplaca = request.form["idplaca"]
        venda.idcliente = int(request.form["idcliente"])
        venda.data = request.form["data"]
        venda.valor_vendido = float(request.form["valor_vendido"])
        venda.forma_pagamento = request.form["forma_pagamento"]

        controller_venda.alterar_venda(venda)
        flash("Venda alterada com sucesso!", "success")
        return redirect(url_for("listar_vendas"))

    venda_dados = controller_venda.pesquisaCodigo(idvenda)
    return render_template("venda/editar.html", titulo="Alterar Venda", venda=venda_dados, veiculos=veiculos, clientes=clientes)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
