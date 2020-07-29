#import all the required libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def reduction (df, components = 93): #preset the number of components to the identified and analysed features
    #declaring the PCA model and the pre-processor
    pca = PCA(n_components = components)
    scaler = StandardScaler()

    scaled = scaler.fit_transform(df) #scale and center the values
    res = pca.fit_transform(scaled) #reducing the variation in the data while also keeping all the parameters
    data = pd.DataFrame(res, columns = df.columns) #return the decomposed values as a dataframe

    return data #return the dataframe