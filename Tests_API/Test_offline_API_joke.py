import pytest
import requests
from unittest.mock import patch

BASE_URL = "https://official-joke-api.appspot.com/random_joke"

def test_no_internet():
    """Testa o comportamento ao simular ausência de internet."""
    with patch("requests.get") as mock_get:
        # Configurando o mock para simular uma falha de conexão
        mock_get.side_effect = requests.ConnectionError("Erro de conexão: Sem acesso à internet.")

        try:
            requests.get(BASE_URL)
        except requests.ConnectionError as e:
            print(f"Teste de conexão falha bem-sucedido: {e}")
        else:
            print("Teste falhou: A exceção esperada não foi levantada.")

