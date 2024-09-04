from fastapi import APIRouter
from model.projeto import *

router_projeto = APIRouter()

@router_projeto.get("/projeto")
async def retornar_projeto():
    return Projeto.buscar_projeto()

@router_projeto.get("/projeto/{id}")
async def retornar_projeto_id(id: int):
    return Projeto.buscar_projeto_id(id=id)

@router_projeto.get("/projeto/{id}/atividade")
async def retornar_atividades_projeto(id: int):
    return Projeto.buscar_atividades_projeto(id=id)

@router_projeto.get("/projeto/{id}/cliente")
async def retornar_clientes_projeto(id: int):
    return Projeto.buscar_clientes_projeto(id=id)

@router_projeto.post("/api/projeto")
async def criar_projeto(body: Projeto):
    return Projeto.criar_projeto(body=body)

@router_projeto.put("/api/projeto/{id}")
async def alterar_projeto(id: int, body: Projeto):
    return Projeto.alterar_projeto(id=id, body=body)

@router_projeto.delete("/api/projeto/{id}")
async def remover_projeto(id: int):
    return Projeto.remover_projeto(id=id)