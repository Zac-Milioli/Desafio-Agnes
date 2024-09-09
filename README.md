# FUNCIONAMENTO

## REST

A documentação da API REST pode ser encontrada em [Documentação REST](https://github.com/Zac-Milioli/Desafio-Agnes/blob/master/docs/Documentação%20REST.pdf)

## BANCO DE DADOS

O banco de dados utilizado é o Postgres. Para o correto funcionamento do sistema, é necessário que o Postgres esteja instalado na máquina e as tabelas criadas de acordo.
O script para criação de tabelas e inserção de dados iniciais pode ser encontrado em [Comandos para Criação das Tabelas](https://github.com/Zac-Milioli/Desafio-Agnes/blob/master/docs/Comandos_criacao_tabelas.sql).

Insira a senha utilizada no banco, nome da database e porta dentro de "conn" nos arquivos:
- backend\src\model\atividade.py
- backend\src\model\cliente.py
- backend\src\model\projeto.py

## BACKEND

Para utilizar o backend, basta navegar até a pasta `backend` usando o terminal
    
```bash
cd backend
```

E então instalar as dependências do projeto

```bash
pip install -r requirements.txt
```

Após instalar as dependências, basta rodar o servidor

```bash
python main.py
```

## FRONTEND

Para utilizar o frontend, basta navegar até a pasta `frontend` usando o terminal

```bash
cd frontend
```

E então instalar as dependências do projeto

```bash
npm install
```

Após instalar as dependências, basta rodar o servidor

```bash
npm run serve
```
