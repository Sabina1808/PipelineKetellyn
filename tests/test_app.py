import sys
import os

# Adiciona o diretório atual ao caminho do Python
sys.path.insert(0, os.getcwd())

from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    

    