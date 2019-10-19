import os
from flask import jsonify, current_app
import numpy as np
from sklearn.linear_model import LinearRegression
from werkzeug.utils import secure_filename
import pandas as pd
import pickle


def linear_regression(file_name, body):
    return jsonify({"output": body})

def pca():
    return jsonify({"output": 'run_pca_success'})
