import os
from flask import jsonify, current_app
import numpy as np
from sklearn.linear_model import LinearRegression
from werkzeug.utils import secure_filename
import pandas as pd

def read_file(file_name):
    data = pd.read_csv(os.path.join(current_app.config['UPLOAD_FOLDER'], file_name + '.csv', ), header=None)

    return jsonify({file_name: data.values.tolist()})

def allowed_file(file_name, allowed_extentions):
    return '.' in file_name and \
           file_name.rsplit('.', 1)[1].lower() in allowed_extentions

def save_file(file):
    filename = secure_filename(file.filename)
    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    # TODO: if save failed?

def upload(file=None):
    ALLOWED_EXTENSIONS = {'csv'}
    if file and allowed_file(file.filename, ALLOWED_EXTENSIONS):
        save_file(file)
        return jsonify({'file_name': file.filename}), 200
    else:
        return jsonify({'error_message': 'Wrong file format'}), 400

def list_files():
    files = os.listdir(current_app.config['UPLOAD_FOLDER'])
    return jsonify({'files': files})

def run_linear_regression(X):
    """
    :param:
    :return:
    """
    # y = 1 * x_0 + 2 * x_1 + 3
    y = np.dot(X, np.array([1, 2])) + 3
    reg = LinearRegression().fit(X, y)
    return jsonify({"output": 'success'})

def run_pca():
    return jsonify({"output": 'run_pca_success'})