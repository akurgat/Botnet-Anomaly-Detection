import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def graph(data):
    
    axis = {'Port_A':'Port_B', 'Total_Packets':'Total_Bytes', 'Bytes_Forward':'Bytes_Backward', 
        'Packets_Forward':'Packets_Backward', 'Rel_Start':'Duration', 'Bits/s_Forward':'Bits/s_Backward'}

    palette = {'Normal':'#32AB60', 'Botnet':'#DB4052'}
    markers = {'Normal':'o', 'Botnet':'X'}

    for x, y in axis.items():
        x_axis = x.replace('_', ' ')
        y_axis = y.replace('_', ' ')

        plt.figure(figsize = (12, 8))
        sns.scatterplot(data = data, x = x, y = y, hue = 'Data', style = 'Data', s = 200, palette = palette, markers = markers)

        plt.title(f'{x_axis} to {y_axis}', fontsize = 22)
        plt.xlabel(f'{x_axis}', fontsize = 15);
        plt.ylabel(f'{y_axis}', fontsize = 15)
        plt.axvline(0, color = 'black')
        plt.axhline(0, color = 'black')
        plt.legend()

    plt.show()