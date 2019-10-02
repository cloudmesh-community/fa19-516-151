from ai_service.server import create_app
from flask import jsonify

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_upload():
    pass

def test_hello(client):
    response = client.get('/hello')
    print(type(response))
    assert response.data == b'Hello, World!'

def test_linear_regression(client):
    response = client.get('/cloudmesh-ai-services/linear-regression')
    assert response.data == b'{"output":"success"}\n'


def test_run_pca(client):
    response = client.get('/cloudmesh-ai-services/pca')

    assert response.data == ''