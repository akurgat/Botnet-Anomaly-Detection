import pandas as pd
import numpy as np

def data_stats_processing(data, columns):

    data.replace([-np.inf, np.inf, np.nan], 0, inplace = True)
    ports = data[['Port_A', 'Port_B', 'Rel_Start']]
    data = data[columns]

    for column in data.columns:
        data[f'{column}_Mean'] = data[column].rolling(2).mean()
        data[f'{column}_EWM'] = data[column].ewm(span = 2).mean()
        data[f'{column}_STD'] = data[column].rolling(2).std()
        data[f'{column}_Diff'] = data[column].diff()
        data[f'{column}_Sum'] = data[column].rolling(2).sum()
        data[f'{column}_Change'] = data[column].pct_change()
        data[f'{column}_Max'] = data[column].rolling(2).max()
        data[f'{column}_Min'] = data[column].rolling(2).min()
        
    data[['Port_A', 'Port_B', 'Rel_Start']] = ports[['Port_A', 'Port_B', 'Rel_Start']]
        
    data.replace([-np.inf, np.inf, np.nan], 0, inplace = True)
    return data