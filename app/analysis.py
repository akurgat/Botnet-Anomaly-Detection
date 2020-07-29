#import all the required libraries
import pandas as pd
import numpy as np

def data_stats_processing(data, columns):
    data.replace([-np.inf, np.inf, np.nan], 0, inplace = True) #impute all the nan values with 0
    ports = data[['Port_A', 'Port_B', 'Rel_Start']] #setting aside the parameters not required for the analysis that shall be returned to the dataframe later
    data = data[columns] #redefine the dataframe with only the colums needed for analysis

    for column in data.columns: #based on the declared columns for analysis calculate the respective statistical parameter and return the values to a new column
        data[f'{column}_Mean'] = data[column].rolling(2).mean() #calculating mean
        data[f'{column}_EWM'] = data[column].ewm(span = 2).mean() #calculating exponemtial moving average
        data[f'{column}_STD'] = data[column].rolling(2).std() #calculating standard deviation
        data[f'{column}_Diff'] = data[column].diff() #calculating difference
        data[f'{column}_Sum'] = data[column].rolling(2).sum() #calculating sum
        data[f'{column}_Change'] = data[column].pct_change() #calculating percentage change
        data[f'{column}_Max'] = data[column].rolling(2).max() #calculating max value
        data[f'{column}_Min'] = data[column].rolling(2).min() #calculating min value
        
    data[['Port_A', 'Port_B', 'Rel_Start']] = ports[['Port_A', 'Port_B', 'Rel_Start']] #restore all the values set aside
        
    data.replace([-np.inf, np.inf, np.nan], 0, inplace = True) #impute all nan and infinite values with 0
    return data #return the dataframe