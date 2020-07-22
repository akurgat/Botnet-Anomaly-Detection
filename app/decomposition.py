import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def reduction (df, components = 93):

    pca = PCA(n_components = components)
    scaler = StandardScaler()

    scaled = scaler.fit_transform(df)
    res = pca.fit_transform(scaled)
    data = pd.DataFrame(res, columns = df.columns)

    return data