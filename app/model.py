import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('model/model-botnet.h5')

def prediction(data):
    
    X = data.values
    y = model.predict(X) 
    y = np.round(y)
    
    return y