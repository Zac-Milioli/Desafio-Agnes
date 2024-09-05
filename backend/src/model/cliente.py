from pydantic import BaseModel
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="desafioagnes",
    user="postgres",
    password="12345"
)
cursor = conn.cursor()

class Cliente(BaseModel):
    nome: str
    projeto_id: int

    @staticmethod
    def buscar_cliente():
        cursor.execute("SELECT * FROM cliente")
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
    def buscar_cliente_id(id: int):
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
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
    def buscar_atividades_cliente(id: int):
        cursor.execute("SELECT * FROM atividade WHERE cliente_id = %s", (id,))
        returned = cursor.fetchall()
        data = []
        for row in returned:
            atividade = {
                'id': row[0],
                'nome': row[1],
                'projeto_id': row[2],
                'cliente_id': row[3]
            }
            data.append(atividade)
        return data
    
    @staticmethod
    def criar_cliente(body):
        cursor.execute("INSERT INTO cliente (nome, projeto_id) VALUES (%s, %s)", (body.nome, body.projeto_id))
        conn.commit()
        return {"message": "Cliente criado com sucesso!"}
    
    @staticmethod
    def alterar_cliente(id: int, body):
        cursor.execute("UPDATE cliente SET nome = %s, projeto_id = %s WHERE id = %s", (body.nome, body.projeto_id, id))
        conn.commit()
        return {"message": "Cliente alterado com sucesso!"}
    
    @staticmethod
    def remover_cliente(id: int):
        cursor.execute("DELETE FROM cliente WHERE id = %s", (id,))
        conn.commit()
        return {"message": "Cliente removido com sucesso!"}