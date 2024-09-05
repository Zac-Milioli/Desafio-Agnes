import requests

BASE_URL = "http://localhost:5000"

def test_criar_atividade():
    response = requests.post(f"{BASE_URL}/api/atividade", json={
        "nome": "Atividade Teste",
        "projeto_id": 1,
        "cliente_id": 1
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Atividade criada com sucesso!"

def test_retornar_atividade():
    response = requests.get(f"{BASE_URL}/atividade")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_retornar_atividade_id():
    response = requests.get(f"{BASE_URL}/atividade/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_alterar_atividade():
    response = requests.put(f"{BASE_URL}/api/atividade/1", json={
        "nome": "Atividade Teste Alterada",
        "projeto_id": 1,
        "cliente_id": 1
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Atividade alterada com sucesso!"

def test_remover_atividade():
    response = requests.delete(f"{BASE_URL}/api/atividade/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Atividade removida com sucesso!"