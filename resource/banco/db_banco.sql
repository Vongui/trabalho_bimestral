create database venda_trb;
use venda_trb;

create table cliente(
	idcliente 	int primary key auto_increment,
    nome 		varchar(60),
    endereco 	varchar(100),
    cidade 		varchar(80),
    uf 			varchar(2),
    cep 		varchar(9)
);

create table veiculo(
	idplaca 		varchar(9) primary key,
    ano 			int,
    modelo 			int,
    preco_fipe 		decimal(10,2),
    fabricante 		varchar(50),
    modelo_veiculo 	varchar(60),
    cor 			varchar(20),
    preco_venda 	decimal(10,2),
    total_despesa 	decimal(10,2),
    status 			int
);

create table compra(
	idcompra 		int primary key auto_increment,
    idplaca 		varchar(9),
    idcliente 		int,
    data			date,
    valor_pago 		decimal(10,2),
    forma_pagamento varchar(40),
    foreign key(idplaca) references veiculo(idplaca),
    foreign key(idcliente) references cliente(idcliente)
);

create table venda(
	idvenda 		int primary key auto_increment,
    idcliente 		int,
    idplaca 		varchar(9),
    data 			date,
    valor_vendido 	decimal(10,2),
    forma_pagamento varchar(40),
    foreign key(idcliente) references cliente(idcliente),
    foreign key(idplaca) references veiculo(idplaca)
);

create table prestador(
	idprestador 	int primary key auto_increment,
    nome_empresa 	varchar(60),
    cidade 			varchar(80),
    uf 				varchar(2),
    cep 			varchar(9)
);

create table despesa(
	iddespesa 		int,
    idplaca 		varchar(9),
    descricao 		varchar(80),
    idprestador 	int,
    data_servico 	date,
    valor 			decimal(8,2),
    primary key(iddespesa, idplaca),
    foreign key(idplaca) references veiculo(idplaca),
    foreign key(idprestador) references prestador(idprestador)
)