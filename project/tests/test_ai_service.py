from server import create_app
from flask import jsonify
import sys
import os
import json
from inspect import signature
from sklearn.linear_model import LinearRegression
from werkzeug.test import EnvironBuilder
from io import StringIO, BytesIO

def test_config():
    """
    Test if configuration of the app is in the testing mode
    :return:
    """
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

class TestUpload:
    def post_file(self,client, path, name):
        f = open(path, 'rb')
        # Simulate post request to upload the file
        response = client.post(path='/cloudmesh-ai-services/upload',
                               data={'file': (f, name)})
        f.close()
        return response.data

    def test_success_upload(self, client):
        """
        Test upload. The file will be uploaded in to the current directory named files
        :param client:
        :return:
        """
        assert self.post_file(client, './test_assets/test_upload.csv','test_upload.csv') \
               == \
               b'{"file_name":"test_upload.csv"}\n'

    def test_format_error(self, client):
        """
        The upload will failed due to the txt file format
        :param client:
        :return:
        """
        assert self.post_file(client, './test_assets/test_upload.csv', 'test_upload.txt') \
               == \
               b'{"error_message":"Wrong file format"}\n'

class TestLinearRegression:
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
                                   'normalize': False,
                                   'n_jobs':1
                               }),
                               content_type='application/json')
        print(response.data)
        assert response.data == b'{"output":{"file_name":"test_upload","fit_intercept":true,"normalize":false}}\n'

    def test_verify_parameters(self):
        pass

def test_run_pca(client):
    response = client.get('/cloudmesh-ai-services/pca')

    assert response.data == ''



