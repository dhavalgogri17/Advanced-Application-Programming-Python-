#!/usr/bin/python

from pymongo import MongoClient
import tornado.web

from tornado.web import HTTPError
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options

from basehandler import BaseHandler
from io import BytesIO
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from PIL import Image
import pickle
from bson.binary import Binary
import json
import base64
import numpy as np
import threading
import io
import cv2
import types
import tempfile

from keras.models import load_model
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten, Activation, BatchNormalization
from keras.optimizers import Adamax
from keras.layers.advanced_activations import LeakyReLU


class PrintHandlers(BaseHandler):
    def get(self):
        '''Write out to screen the handlers used
        This is a nice debugging example!
        '''
        self.set_header("Content-Type", "application/json")
        self.write(self.application.handlers_string.replace('),', '),\n'))




class PredictOneFromDatasetId(BaseHandler):

    def readb64(self, base64_string):
        sbuf = BytesIO()
        sbuf.write(base64.b64decode(base64_string))
        pimg = Image.open(sbuf)
        pimg = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)
        return cv2.resize(pimg, (100, 100)) 


    def predict(self):
        data = json.loads(self.request.body.decode("utf-8"))

        img = self.readb64(data['feature'])

        # imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # ret,thresh = cv2.threshold(imgray,175,255,0)
        # im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(img, contours, -1, (0,255,0), 3)

        f = np.array(img)
        f = f / 255
        f = np.expand_dims(f, axis=0)
        # f.reshape(1,100*100*3)


        dsid = data['dsid']

        # load the model from the database (using pickle)
        # we are blocking tornado!! no!!
        if dsid not in self.clf:
            print('Loading Model From DB')
            tmp = self.db.models.find_one({"dsid": dsid})
            model_name = tmp['model']
            self.clf[dsid] = load_model(model_name)

        if "id_to_label" not in self.clf:
            print('Loading id_to_label From DB')
            tmp = self.db.models.find_one({"dsid": dsid})
            id_to_label = tmp['id_to_label']
            self.clf['id_to_label'] = {int(k): v for k, v in id_to_label.items()}

        preddiction_one_hot = self.clf[dsid].predict(f, batch_size=1, verbose=1)
        print("preddiction one hot encoded: ",preddiction_one_hot)
        predLabel = self.clf["id_to_label"][np.argmax(preddiction_one_hot, axis=None, out=None)]

        print("Predicted Label = %s" % predLabel)
        self.write_json({"prediction": str(predLabel)})
        self.finish()


    # this annotation helps us manually call the finish functions, so we call it after we are ready to write the data back to the client
    @tornado.web.asynchronous
    def post(self):
        '''Predict the class of a sent feature vector
        '''

        # spawing a new thread which calls the app_point function above
        predict_thread = threading.Thread(target=self.predict, args=())
        predict_thread.start()
