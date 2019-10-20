import os
from flask import jsonify, current_app
import numpy as np
from sklearn.linear_model import LinearRegression
from werkzeug.utils import secure_filename

def linear_regression(file_name, body):
    paras = body['paras']

    try:
        LinearRegression(**paras)
    except Exception as e:
        return jsonify({'error_message': str(e)})

    return jsonify({"output": body})

def pca():
    return jsonify({"output": 'run_pca_success'})

