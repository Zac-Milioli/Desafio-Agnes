from fastapi import APIRouter
from model.atividade import *

router_atividade = APIRouter()

@router_atividade.get("/atividade")
async def retornar_atividade():
    return Atividade.buscar_atividade()

@router_atividade.get("/atividade/{id}")
async def retornar_atividade_id(id: int):
    return Atividade.buscar_atividade_id(id=id)

@router_atividade.post("/api/atividade")
async def criar_atividade(body: Atividade):
    return Atividade.criar_atividade(body=body)

@router_atividade.put("/api/atividade/{id}")
async def alterar_atividade(id: int, body: Atividade):
    return Atividade.alterar_atividade(id=id, body=body)

@router_atividade.delete("/api/atividade/{id}")
async def remover_atividade(id: int):
    return Atividade.remover_atividade(id=id)