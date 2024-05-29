import requests
import json

# Endpoints da API
BASE_URL = 'http://127.0.0.1:5000/api/v1'
AUTH = ('admin', 'admin')

def test_producao():
    """Testa o endpoint de produção."""
    # Testa sem filtros
    response = requests.get(f'{BASE_URL}/producao', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de ano
    response = requests.get(f'{BASE_URL}/producao?ano=2023', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de controle
    response = requests.get(f'{BASE_URL}/producao?control=vinho_mesa_tinto', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de litros
    response = requests.get(f'{BASE_URL}/producao?litros_min=1000&litros_max=2000', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_comercial():
    """Testa o endpoint de comercialização."""
    # Testa sem filtros
    response = requests.get(f'{BASE_URL}/comercial', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de ano
    response = requests.get(f'{BASE_URL}/comercial?ano=2023', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de controle
    response = requests.get(f'{BASE_URL}/comercial?control=vinho_mesa_tinto', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de litros
    response = requests.get(f'{BASE_URL}/comercial?litros_min=1000&litros_max=2000', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_importacao():
    """Testa o endpoint de importação."""
    # Testa com tipo inválido
    response = requests.get(f'{BASE_URL}/importacao/invalido', auth=AUTH)
    assert response.status_code == 400

    # Testa com tipo válido
    for tipo in ['espumante', 'frescas', 'passas', 'suco', 'vinho']:
        response = requests.get(f'{BASE_URL}/importacao/{tipo}', auth=AUTH)
        assert response.status_code == 200
        assert len(response.json()) > 0

    # Testa com filtro de ano
    response = requests.get(f'{BASE_URL}/importacao/vinho?ano=2023', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de país
    response = requests.get(f'{BASE_URL}/importacao/vinho?pais=argentina', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de dolar
    response = requests.get(f'{BASE_URL}/importacao/vinho?dolar_min=1000&dolar_max=2000', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de kg
    response = requests.get(f'{BASE_URL}/importacao/vinho?kg_min=1000&kg_max=2000', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_exportacao():
    """Testa o endpoint de exportação."""
    # Testa com tipo inválido
    response = requests.get(f'{BASE_URL}/exportacao/invalido', auth=AUTH)
    assert response.status_code == 400

    # Testa com tipo válido
    for tipo in ['espumante', 'suco', 'uva', 'vinho']:
        response = requests.get(f'{BASE_URL}/exportacao/{tipo}', auth=AUTH)
        assert response.status_code == 200
        assert len(response.json()) > 0

    # Testa com filtro de ano
    response = requests.get(f'{BASE_URL}/exportacao/vinho?ano=2023', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de país
    response = requests.get(f'{BASE_URL}/exportacao/vinho?pais=franca', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de dolar
    response = requests.get(f'{BASE_URL}/exportacao/vinho?dolar_min=1000&dolar_max=2000', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de kg
    response = requests.get(f'{BASE_URL}/exportacao/vinho?kg_min=1000&kg_max=2000', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_processa():
    """Testa o endpoint de processamento."""
    # Testa com tipo inválido
    response = requests.get(f'{BASE_URL}/processa/invalido', auth=AUTH)
    assert response.status_code == 400

    # Testa com tipo válido
    for tipo in ['americanas_hibridas', 'sem_classificacao', 'uvas_mesa', 'viniferas']:
        response = requests.get(f'{BASE_URL}/processa/{tipo}', auth=AUTH)
        assert response.status_code == 200
        assert len(response.json()) > 0

    # Testa com filtro de ano
    response = requests.get(f'{BASE_URL}/processa/viniferas?ano=2023', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de controle
    response = requests.get(f'{BASE_URL}/processa/viniferas?control=tintas_oberlin', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Testa com filtro de kg
    response = requests.get(f'{BASE_URL}/processa/viniferas?kg_min=1000&kg_max=2000', auth=AUTH)
    assert response.status_code == 200
    assert len(response.json()) > 0

# Executa os testes
if __name__ == '__main__':
    test_producao()
    test_comercial()
    test_importacao()
    test_exportacao()
    test_processa()

    print('Todos os testes foram executados com sucesso!')