from __future__ import print_function

import numpy as np
import cv2
from keras.models import model_from_json


class Flower:
    def __init__(self, name, areas):
        self.name = name
        self.areas = areas


def recognitionFlower(pathImage):

    flowers = [
        Flower('bluebell', ['Tropical Rainforest', 'Temperate']),
        Flower('buttercup', ['Grassland and Meadow']),
        Flower('coltsfoot', ['Grassland and Meadow']),
        Flower('cowslip', ['Grassland and Meadow']),
        Flower('crocus', ['Grassland and Meadow', 'Temperate']),
        Flower('daffodil', ['Temperate', 'Subtropical']),
        Flower('daisy', ['Grassland and Meadow', 'Temperate']),
        Flower('dandelion', ['Grassland and Meadow', 'Temperate']),
        Flower('fritillary', ['Grassland and Meadow']),
        Flower('iris', ['Temperate', 'Subtropical']),
        Flower('lilyvalley', ['Subtropical', 'Temperate']),
        Flower('pansy', ['Grassland and Meadow', 'Temperate']),
        Flower('snowdrop', ['Temperate']),
        Flower('sunflower', ['Desert']),
        Flower('tigerlily', ['Subtropical']),
        Flower('tulip', ['Grassland and Meadow', 'Temperate', 'Subtropical']),
        Flower('windflower', ['Grassland and Meadow', 'Temperate']),
    ]

    json_file = open('feature/recognition/model/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("feature/recognition/model/model.h5")
    img = cv2.imread(pathImage)
    faceAligned = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
    faceAligned = np.array(faceAligned)
    faceAligned = faceAligned.astype('float32')
    faceAligned = np.expand_dims(faceAligned, axis=0)
    faceAligned /= 255.0
    Y_pred = model.predict(faceAligned)

    predictions = [(flowers[index], value) for index, value in enumerate(Y_pred[0]) if value >= 0.01]
    predictions.sort(key=lambda x: x[1], reverse=True)

    return [{'name_flower': item[0].name, 'areas': item[0].areas, 'match_rate': int(item[1] * 100)} for item in
            predictions]
