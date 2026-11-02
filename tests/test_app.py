import sys
import os

# Adiciona o diretório raiz ao caminho de busca de módulos do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    
    