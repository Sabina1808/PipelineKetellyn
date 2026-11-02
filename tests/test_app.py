import os
import sys

# Adiciona a pasta raiz do projeto ao caminho de importação do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


    