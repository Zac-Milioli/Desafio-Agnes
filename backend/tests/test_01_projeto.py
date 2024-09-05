import requests

BASE_URL = "http://localhost:5000"

def test_criar_projeto():
    response = requests.post(f"{BASE_URL}/api/projeto", json={
        "nome": "Projeto Teste",
        "status": "Em andamento"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Projeto criado com sucesso!"

def test_retornar_projeto():
    response = requests.get(f"{BASE_URL}/projeto")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_retornar_projeto_id():
    response = requests.get(f"{BASE_URL}/projeto/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_alterar_projeto():
    response = requests.put(f"{BASE_URL}/api/projeto/1", json={
        "nome": "Projeto Teste Alterado",
        "status": "Concluído"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Projeto alterado com sucesso!"

def test_remover_projeto():
    response = requests.delete(f"{BASE_URL}/api/projeto/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Projeto removido com sucesso!"