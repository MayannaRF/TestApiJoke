# Joke API Testing Suite

## 📋 Projeto

Este repositório contém um conjunto de testes automatizados para a **Joke API**, que fornece piadas aleatórias através do endpoint público [https://official-joke-api.appspot.com/random_joke](https://official-joke-api.appspot.com/random_joke). O objetivo principal é validar a funcionalidade e performance, garantindo uma experiência consistente e confiável para seus usuários.

---
## 🗂️ Estrutura do Repositório
```
|--  TestAPIjoke
|    |--  Tests_API 
|         |--  Test_API_joke.py         
|         |--  Test_load_API_joke.py   
|         |--  Test_offline_API_joke.py
|
|    |--   README.md              
```
---
## ⚙️ Tetes realizados 

- **Test_API_joke**:
  - Verifica se o endpoint responde com o código de status HTTP 200.
  - Garanti que a resposta esteja no formato JSON e contenha todos os campos obrigatórios (type, setup, punchline, id).
  - Verifica se cada campo da resposta possui o tipo de dado correto.
  - Verifica se os campos type, setup e punchline não estão vazios.
  - Verifica se os IDs retornados são únicos em 100 requisições consecutivas.
  - Verifica se comportamento da API ao acessar um endpoint inválido.
  - Mede o tempo de resposta da API e verifica se é inferior a 500ms.

- **Test_load_API_joke**:
  - Avaliar o comportamento da API quando submetida a múltiplas requisições simultâneas.

- **Test_offline_API_joke**:
  - Verificar o comportamento da API ao acesso offline.

---

## 🛠️ Pré-requisitos

- Premissas
  - A API deve estar disponível durante os testes.
  - A estrutura JSON da resposta não deve mudar sem aviso prévio.
    
- Antes de executar os testes, verifique se você possui os seguintes requisitos instalados:
  - **Python 3.8+**
  - **Bibliotecas necessárias**:
    - `requests`
    - `concurrent.futures` (incluso no Python padrão)
    - `unittest.mock` (incluso no Python padrão)

    Para instalar o pacote `requests`, utilize:

    ```bash
    pip install requests
    ```

---
## 📝 Documentação
- Documentação dos Casos de Testes da API Joke
(https://docs.google.com/document/d/1d3K-NGseD-BVCTcGZ0Ed8v3ZsDc0RTcg1LGp6jHj4G0/edit?usp=sharing)

---

## 📊 Relatórios de Testes
- Relatório de Resultados dos Testes
(https://docs.google.com/document/d/1KRofNtdrLL1dx7KJuyFw3sKWzpCgstBsgLFYUbESaCU/edit?usp=sharing)


