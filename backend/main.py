from fastapi import FastAPI
from src.routes import atividade_routes, cliente_routes, projeto_routes
import uvicorn

app = FastAPI()
app.include_router(atividade_routes.router_atividade)
app.include_router(cliente_routes.router_cliente)
app.include_router(projeto_routes.router_projeto)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)