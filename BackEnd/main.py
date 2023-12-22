# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import os

from flask import Flask, request, jsonify

from feature.description import callGpt
from model.Flower import Flower
from feature.recognition.recognitionFlower import recognitionFlower

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


@app.route('/recognition', methods=['POST', 'GET'])
def recognition():
    if request.method == 'POST':
        file = request.files['file']
        file_path = os.path.join(
            'feature/recognition/imageReceive/', file.filename)
        file.save(file_path)

        flowers = recognitionFlower(file_path)

        response = {
            'status': 'success',
            'message': 'File uploaded successfully',
            'results': flowers
        }

        return jsonify(response), 200
    else:
        response = {
            'status': 'error',
            'message': 'No file uploaded'
        }
        return jsonify(response), 400


@app.route('/description/<nameFlower>', methods=['GET'])
def descriptionFlower(nameFlower):
    if request.method == 'GET':
        flower = Flower(
            nameFlower,
            callGpt.callGPT("Description " + nameFlower),
            callGpt.callGPT("List species " + nameFlower),
            callGpt.callGPT("How to care " + nameFlower)
        )
        response = {
            'status': 'success',
            'message': 'Description ' + nameFlower,
            'flower': flower.__dict__
        }

        return jsonify(response), 200
    else:
        response = {
            'status': 'error',
            'message': "Server can't get name flower"
        }
        return jsonify(response), 400


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="172.16.4.235")
