from ai_service.server import create_app
from flask import jsonify
import sys
import os
import json
sys.path.append(os.path.dirname(os.getcwd()))
from inspect import signature
from sklearn.linear_model import LinearRegression
def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_upload():
    pass

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'

class TestLinearRegression():
    def test_parameter_passing(self, client):
        """
        Testing the parameter passing. The users are able to passing a number of arguments via json.
        :param client: the flask test client
        :return:
        """
        response = client.post(path='/cloudmesh-ai-services/linear-regression/test_upload',
                               data=json.dumps({
                                   'file_name': 'test_upload',
                                   'fit_intercept': True,
                                   'normalize': False
                               }),
                               content_type='application/json')
        assert response.data == b'{"output":"success"}\n'

    def test_json(self):
        print(json.dumps({'file': 'csv'}))

    def test_get_function_signature(self):
        print(signature(LinearRegression))
def test_run_pca(client):
    response = client.get('/cloudmesh-ai-services/pca')

    assert response.data == ''



