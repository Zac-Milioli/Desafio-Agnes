from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import atividade_routes, cliente_routes, projeto_routes
import uvicorn

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens. Modifique conforme necessário.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP. Modifique conforme necessário.
    allow_headers=["*"],  # Permite todos os cabeçalhos. Modifique conforme necessário.
)

app.include_router(atividade_routes.router_atividade)
app.include_router(cliente_routes.router_cliente)
app.include_router(projeto_routes.router_projeto)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)