from flask import jsonify
import numpy as np
from sklearn.linear_model import LinearRegression


def allowed_file(filename, allowed_extentions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extentions

def upload(file=None):
    ALLOWED_EXTENSIONS = {'csv'}
    if allowed_file(file.filename, ALLOWED_EXTENSIONS):
        file_name = file.filename


        return jsonify({'file_name': file_name}), 200
    else:
        return jsonify({'error_message': 'Wrong file format'}), 400

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