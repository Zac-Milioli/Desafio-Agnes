import requests

BASE_URL = "http://localhost:5000"

def test_criar_cliente():
    response = requests.post(f"{BASE_URL}/api/cliente", json={
        "nome": "Cliente Teste",
        "projeto_id": 1
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Cliente criado com sucesso!"

def test_retornar_cliente():
    response = requests.get(f"{BASE_URL}/cliente")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_retornar_cliente_id():
    response = requests.get(f"{BASE_URL}/cliente/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_alterar_cliente():
    response = requests.put(f"{BASE_URL}/api/cliente/1", json={
        "nome": "Cliente Teste Alterado",
        "projeto_id": 1
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Cliente alterado com sucesso!"

def test_remover_cliente():
    response = requests.delete(f"{BASE_URL}/api/cliente/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Cliente removido com sucesso!"