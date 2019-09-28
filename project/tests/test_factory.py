from ai_service.server import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'

def test_linear_regression(client):
    response = client.get('/cloudmesh-ai-services/linear-regression')
    assert response.data == b'{"output":"success"}\n'