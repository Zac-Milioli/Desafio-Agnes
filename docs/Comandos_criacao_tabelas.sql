CREATE TABLE projeto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    status VARCHAR(255) NOT NULL
);

CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    projeto_id INT NOT NULL REFERENCES projeto(id) ON DELETE CASCADE
);

CREATE TABLE atividade (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    projeto_id INT NOT NULL REFERENCES projeto(id) ON DELETE CASCADE,
    cliente_id INT NOT NULL REFERENCES cliente(id) ON DELETE CASCADE
);

-- Inserção de Projetos
INSERT INTO projeto (nome, status) VALUES ('Projeto Alpha', 'Em andamento');
INSERT INTO projeto (nome, status) VALUES ('Projeto Beta', 'Concluído');
INSERT INTO projeto (nome, status) VALUES ('Projeto Gamma', 'Cancelado');

-- Inserção de Clientes
INSERT INTO cliente (nome, projeto_id) VALUES ('Cliente 1', 1);
INSERT INTO cliente (nome, projeto_id) VALUES ('Cliente 2', 1);
INSERT INTO cliente (nome, projeto_id) VALUES ('Cliente 3', 2);
INSERT INTO cliente (nome, projeto_id) VALUES ('Cliente 4', 2);
INSERT INTO cliente (nome, projeto_id) VALUES ('Cliente 5', 3);
INSERT INTO cliente (nome, projeto_id) VALUES ('Cliente 6', 3);
INSERT INTO cliente (nome, projeto_id) VALUES ('Cliente 7', 1);
INSERT INTO cliente (nome, projeto_id) VALUES ('Cliente 8', 2);

-- Inserção de Atividades
INSERT INTO atividade (nome, projeto_id, cliente_id) VALUES ('Atividade A1', 1, 1);
INSERT INTO atividade (nome, projeto_id, cliente_id) VALUES ('Atividade A2', 1, 2);
INSERT INTO atividade (nome, projeto_id, cliente_id) VALUES ('Atividade B1', 2, 3);
INSERT INTO atividade (nome, projeto_id, cliente_id) VALUES ('Atividade B2', 2, 4);
INSERT INTO atividade (nome, projeto_id, cliente_id) VALUES ('Atividade C1', 3, 5);
INSERT INTO atividade (nome, projeto_id, cliente_id) VALUES ('Atividade C2', 3, 6);
INSERT INTO atividade (nome, projeto_id, cliente_id) VALUES ('Atividade A3', 1, 7);
INSERT INTO atividade (nome, projeto_id, cliente_id) VALUES ('Atividade B3', 2, 8);