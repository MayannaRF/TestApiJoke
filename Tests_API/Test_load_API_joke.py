import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://official-joke-api.appspot.com/random_joke"
NUM_USERS = 10
# Número de usuários simultâneos


def fetch_joke(user_id):
    """Simula um usuário buscando uma piada."""
    start_time = time.time()  # Marca o início da requisição
    try:
        response = requests.get(BASE_URL, timeout=5)  # Timeout de 5 segundos
        elapsed_time = time.time() - start_time  # Tempo de resposta
        if response.status_code == 200:
            joke = response.json()
            # Validação básica da consistência da resposta
            if all(key in joke for key in ["type", "setup", "punchline", "id"]):
                return (user_id, elapsed_time, "Success")
            else:
                return (user_id, elapsed_time, "Invalid Response Structure")
        else:
            return (user_id, elapsed_time, f"HTTP Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        elapsed_time = time.time() - start_time
        return (user_id, elapsed_time, f"Error: {e}")


def run_load_test():
    """Executa o teste de carga com múltiplos usuários simultâneos."""
    print(f"Simulando {NUM_USERS} usuários simultâneos...\n")
    results = []
    with ThreadPoolExecutor(max_workers=NUM_USERS) as executor:
        futures = {executor.submit(fetch_joke, user_id): user_id for user_id in range(NUM_USERS)}
        for future in as_completed(futures):
            user_id = futures[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                results.append((user_id, None, f"Unhandled Exception: {e}"))

    # Exibindo os resultados
    total_time = 0
    success_count = 0
    for user_id, elapsed_time, status in results:
        print(f"User {user_id}: {status} (Response Time: {elapsed_time:.2f}s)")
        if status == "Success":
            success_count += 1
        total_time += elapsed_time if elapsed_time else 0

    avg_time = total_time / NUM_USERS
    print("\n--- Resumo ---")
    print(f"Usuários testados: {NUM_USERS}")
    print(f"Sucessos: {success_count}/{NUM_USERS}")
    print(f"Tempo médio de resposta: {avg_time:.2f}s")


if __name__ == "__main__":
    run_load_test()