# -*- coding: UTF-8 -*-
import app.model as model
import numpy as np

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def getResult():
    input = np.array([[5.5, 2.4, 2.7, 1.]])
    result = model.predict(input)
    return jsonify({'result': str(result)})

@app.route('/predict', methods=['POST'])
def postInput():
    insertValues = request.get_json()
    x1=insertValues['file_name']
    globals.img = str(x1)

    result = model.predict(globals.img)
    return str(result)
    #return jsonify({'return': str(globals.img)})
