import pytest
import requests

BASE_URL = "https://official-joke-api.appspot.com/random_joke"

def test_status_code():
    """Testa se o endpoint retorna o status code 200."""
    response = requests.get(BASE_URL)
    assert response.status_code == 200, f"Erro: Status code esperado era 200, mas foi {response.status_code}."


def test_response_format():
    """Testa se a resposta está no formato JSON e contém os campos obrigatórios."""
    response = requests.get(BASE_URL)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8", "Erro: Resposta não está no formato JSON."
    json_data = response.json()
    for field in ["type", "setup", "punchline", "id"]:
        assert field in json_data, f"Erro: Campo '{field}' ausente na resposta."


def test_field_types():
    """Testa se os campos têm os tipos de dados corretos."""
    response = requests.get(BASE_URL)
    json_data = response.json()
    assert isinstance(json_data["type"], str), "Erro: Campo 'type' não é string."
    assert isinstance(json_data["setup"], str), "Erro: Campo 'setup' não é string."
    assert isinstance(json_data["punchline"], str), "Erro: Campo 'punchline' não é string."
    assert isinstance(json_data["id"], int), "Erro: Campo 'id' não é inteiro."


def test_no_empty_fields():
    """Testa se nenhum campo está vazio."""
    response = requests.get(BASE_URL)
    json_data = response.json()
    for field in ["type", "setup", "punchline"]:
        assert json_data[field].strip(), f"Erro: Campo '{field}' está vazio."


def test_unique_ids():
    """Testa se os IDs são únicos em 100 requisições."""
    ids = set()
    for _ in range(100):
        response = requests.get(BASE_URL)
        json_data = response.json()
        assert json_data["id"] not in ids, f"Erro: ID duplicado encontrado: {json_data['id']}"
        ids.add(json_data["id"])
    print(f"Testado: {len(ids)} IDs únicos encontrados em 100 requisições.")


def test_ainvalid_endpoint():
    """Testa um endpoint inválido para validar a resposta de erro."""
    invalid_url = "https://official-joke-api.appspot.com/random_joke_invalid"
    response = requests.get(invalid_url)
    assert response.status_code == 404, f"Erro: Status code esperado era 404, mas foi {response.status_code}."


def test_response_time():
    """Testa se o tempo de resposta é inferior a 500ms."""
    response = requests.get(BASE_URL)
    assert response.elapsed.total_seconds() < 0.5, "Erro: Tempo de resposta maior que 500ms."