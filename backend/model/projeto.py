from pydantic import BaseModel
from enum import Enum
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="desafioagnes",
    user="postgres",
    password="12345"
)
cursor = conn.cursor()

class StatusProjeto(Enum):
    EM_ANDAMENTO = "Em andamento"
    CONCLUIDO = "Concluído"
    CANCELADO = "Cancelado"

class Projeto(BaseModel):
    nome: str
    status: StatusProjeto

    @staticmethod
    def buscar_projeto():
        cursor.execute("SELECT * FROM projeto")
        returned = cursor.fetchall()
        data = []
        for row in returned:
            projeto = {
                'id': row[0],
                'nome': row[1],
                'status': row[2]
            }
            data.append(projeto)
        return data

    @staticmethod
    def buscar_projeto_id(id: int):
        cursor.execute("SELECT * FROM projeto WHERE id = %s", (id,))
        returned = cursor.fetchall()
        data = []
        for row in returned:
            projeto = {
                'id': row[0],
                'nome': row[1],
                'status': row[2]
            }
            data.append(projeto)
        return data
    
    @staticmethod
    def buscar_atividades_projeto(id: int):
        cursor.execute("SELECT * FROM atividade WHERE projeto_id = %s", (id,))
        returned = cursor.fetchall()
        data = []
        for row in returned:
            atividade = {
                'id': row[0],
                'nome': row[1],
                'projeto_id': row[2]
            }
            data.append(atividade)
        return data
    
    @staticmethod
    def buscar_clientes_projeto(id: int):
        cursor.execute("SELECT * FROM cliente WHERE projeto_id = %s", (id,))
        returned = cursor.fetchall()
        data = []
        for row in returned:
            cliente = {
                'id': row[0],
                'nome': row[1],
                'projeto_id': row[2]
            }
            data.append(cliente)
        return data
    
    @staticmethod
    def criar_projeto(body):
        try:
            status = StatusProjeto(body.status)
        except ValueError:
            return {"message": f"Invalid status: {body.status}. Must be one of {[status.value for status in StatusProjeto]}"}
        cursor.execute("INSERT INTO projeto (nome, status) VALUES (%s, %s)", (body.nome, status.value))
        conn.commit()
        return {"message": "Projeto criado com sucesso!"}

    @staticmethod
    def alterar_projeto(id: int, body):
        try:
            status = StatusProjeto(body.status)
        except ValueError:
            return {"message": f"Invalid status: {body.status}. Must be one of {[status.value for status in StatusProjeto]}"}
        cursor.execute("UPDATE projeto SET nome = %s, status = %s WHERE id = %s", (body.nome, status.value, id))
        conn.commit()
        return {"message": "Projeto alterado com sucesso!"}
    
    @staticmethod
    def remover_projeto(id: int):
        cursor.execute("DELETE FROM projeto WHERE id = %s", (id,))
        conn.commit()
        return {"message": "Projeto removido com sucesso!"}