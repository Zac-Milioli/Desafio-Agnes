from fastapi import APIRouter
from model.cliente import *

router_cliente = APIRouter()

@router_cliente.get("/cliente")
async def retornar_cliente():
    return Cliente.buscar_cliente()

@router_cliente.get("/cliente/{id}")
async def retornar_cliente_id(id: int):
    return Cliente.buscar_cliente_id(id=id)

@router_cliente.get("/cliente/{id}/atividade")
async def retornar_atividades_cliente(id: int):
    return Cliente.buscar_atividades_cliente(id=id)

@router_cliente.post("/api/cliente")
async def criar_cliente(body: Cliente):
    return Cliente.criar_cliente(body=body)

@router_cliente.put("/api/cliente/{id}")
async def alterar_cliente(id: int, body: Cliente):
    return Cliente.alterar_cliente(id=id, body=body)

@router_cliente.delete("/api/cliente/{id}")
async def remover_cliente(id: int):
    return Cliente.remover_cliente(id=id)