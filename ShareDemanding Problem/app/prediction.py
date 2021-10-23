import numpy as np
import pickle

class PickledModel():

    model = pickle.load(open('model.sav', 'rb'))

    def SimplePred(self, data):
        return self.__model.predict([data])