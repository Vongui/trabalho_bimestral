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
);

INSERT INTO cliente (nome, endereco, cidade, uf, cep) VALUES
('João Silva', 'Rua A, 123', 'São Paulo', 'SP', '01000-000'),
('Maria Oliveira', 'Avenida B, 456', 'Rio de Janeiro', 'RJ', '20000-000'),
('Carlos Pereira', 'Praça C, 789', 'Belo Horizonte', 'MG', '30000-000'),
('Ana Santos', 'Rua D, 101', 'Curitiba', 'PR', '80000-000'),
('Fernanda Lima', 'Rua E, 202', 'Porto Alegre', 'RS', '90000-000');

INSERT INTO veiculo (idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa, status) VALUES
('ABC1D23', 2020, 1, 50000.00, 'Volkswagen', 'Gol', 'Preto', 48000.00, 0.00, 0),
('DEF4G56', 2019, 2, 60000.00, 'Fiat', 'Palio', 'Branco', 58000.00, 0.00, 0),
('GHI7H89', 2021, 3, 70000.00, 'Chevrolet', 'Onix', 'Vermelho', 68000.00, 0.00, 0),
('JKL0M12', 2018, 4, 80000.00, 'Ford', 'Fiesta', 'Azul', 78000.00, 0.00, 0),
('NOP3Q45', 2022, 5, 90000.00, 'Honda', 'Civic', 'Cinza', 88000.00, 0.00, 0);

INSERT INTO prestador (nome_empresa, cidade, uf, cep) VALUES
('Serviços Automotivos LTDA', 'São Paulo', 'SP', '01000-001'),
('Oficina Mecânica do João', 'Rio de Janeiro', 'RJ', '20000-001'),
('Auto Peças e Serviços', 'Belo Horizonte', 'MG', '30000-001'),
('Mecânica da Ana', 'Curitiba', 'PR', '80000-001'),
('Reformas e Manutenções', 'Porto Alegre', 'RS', '90000-001');