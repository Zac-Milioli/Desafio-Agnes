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

class Atividade(BaseModel):
        nome: str
        projeto_id: int
        cliente_id: int
        
        @staticmethod
        def buscar_atividade():
                cursor.execute("SELECT * FROM atividade")
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
        def buscar_atividade_id(id: int):
                cursor.execute("SELECT * FROM atividade WHERE id = %s", (id,))
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
        def criar_atividade(body):
                cursor.execute("INSERT INTO atividade (nome, projeto_id, cliente_id) VALUES (%s, %s, %s)", (body.nome, body.projeto_id, body.cliente_id))
                conn.commit()
                return {"message": "Atividade criada com sucesso!"}
        
        @staticmethod
        def alterar_atividade(id: int, body):
                cursor.execute("UPDATE atividade SET nome = %s, projeto_id = %s, cliente_id = %s WHERE id = %s", (body.nome, body.projeto_id, body.cliente_id, id))
                conn.commit()
                return {"message": "Atividade alterada com sucesso!"}

        @staticmethod
        def remover_atividade(id: int):
                cursor.execute("DELETE FROM atividade WHERE id = %s", (id,))
                conn.commit()
                return {"message": "Atividade removida com sucesso!"}