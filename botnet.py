from app.analysis import *
from app.decomposition import *
from app.plot import *
from app.model import *

def main():

    global df

    df.set_index(['Address_A', 'Address_B'], inplace = True)
    df.sort_values(by = ['Rel_Start'], inplace = True)

    df['Download_Upload_Ratio'] = df['Bits/s_Forward']/df['Bits/s_Backward']
    numeric_columns = ['Port_A', 'Port_B', 'Total_Packets', 'Total_Bytes', 'Packets_Forward', 'Bytes_Forward',
                    'Packets_Backward', 'Bytes_Backward', 'Duration', 'Bits/s_Forward', 'Bits/s_Backward']
    statistical_columns = ['Total_Packets', 'Total_Bytes', 'Packets_Forward', 'Bytes_Forward', 'Packets_Backward', 
                        'Bytes_Backward', 'Duration', 'Bits/s_Forward', 'Bits/s_Backward', 'Download_Upload_Ratio']

    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)
    df = data_stats_processing(df, statistical_columns)
    df_reduced = reduction(df)
    df['Predictions'] = prediction(df_reduced)

    prediction_map = {0:'Normal', 1:'Botnet'}
    df['Data'] = df['Predictions'].map(prediction_map)
    botnets = df[df['Data'] == 'Botnet']

    for source_ip, destination_ip in botnets.index.unique():
        print ('Suspected Botnet IP Address: \t ', source_ip)
        print ('Targeted IP Address: \t\t ', destination_ip)

    graph(df)

if __name__ == '__main__':

    import warnings
    warnings.filterwarnings('ignore')

    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--file', required = True, help = 'Enter the path to the TCP/UDP csv file')
    args = vars(ap.parse_args())

    df  = pd.read_csv(args['file'])
    main()