#the main app

#import all the required modules and their functions
from app.analysis import *
from app.decomposition import *
from app.plot import *
from app.model import *

def main():

    global df #use the declared file

    #use the IP address ash the unique identifier for each data point and sort them according to the relative start time in ascending order
    df.set_index(['Address_A', 'Address_B'], inplace = True)
    df.sort_values(by = ['Rel_Start'], inplace = True)

    df['Download_Upload_Ratio'] = df['Bits/s_Forward']/df['Bits/s_Backward'] #calculating the download ratio values

    #ensure all the parameters used in the analysis are numeric
    numeric_columns = ['Port_A', 'Port_B', 'Total_Packets', 'Total_Bytes', 'Packets_Forward', 'Bytes_Forward',
                    'Packets_Backward', 'Bytes_Backward', 'Duration', 'Bits/s_Forward', 'Bits/s_Backward']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)

    #identify all the parameters needed for further analysis
    statistical_columns = ['Total_Packets', 'Total_Bytes', 'Packets_Forward', 'Bytes_Forward', 'Packets_Backward', 
                        'Bytes_Backward', 'Duration', 'Bits/s_Forward', 'Bits/s_Backward', 'Download_Upload_Ratio']
    df = data_stats_processing(df, statistical_columns) #analysing the parameters defined above

    df_reduced = reduction(df) #decompose the variables
    df['Predictions'] = prediction(df_reduced) #use the decomposed variables to make the predictions

    prediction_map = {0:'Normal', 1:'Botnet'} #replace the values from the predictions repsectively; 0 for Normal and 1 for Botnet
    df['Data'] = df['Predictions'].map(prediction_map)
    botnets = df[df['Data'] == 'Botnet'] #filter only the botnet parameters identified

    for source_ip, destination_ip in botnets.index.unique(): #identify the uinique source destination ip pairs and print them out
        print ('Suspected Botnet IP Address: \t ', source_ip)
        print ('Targeted IP Address: \t\t ', destination_ip)

    graph(df) #graph the whole data set on the basis of the predictions

if __name__ == '__main__': #steps taken when the app is initialized

    import warnings
    warnings.filterwarnings('ignore') #ignore all warnings

    #define the file address and file name as the argument file for analysis
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--file', required = True, help = 'Enter the path to the TCP/UDP csv file')
    args = vars(ap.parse_args())

    df  = pd.read_csv(args['file']) #set the declared file as df
    main() #run the app