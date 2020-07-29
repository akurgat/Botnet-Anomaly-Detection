#import all the required libraries
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('model/model-botnet.h5') #loading the model

def prediction(data):
    
    X = data.values #converting analysed parameters to a numpy array
    y = model.predict(X) #using the model to make the predictions
    y = np.round(y) #rounding off the predictions to 0 deciaml points
    
    return y #delivering the predictions