#import all the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def graph(data):
    #pairing all the relavant parameters to the oringial set of features in the file
    axis = {'Port_A':'Port_B', 'Total_Packets':'Total_Bytes', 'Bytes_Forward':'Bytes_Backward', 
        'Packets_Forward':'Packets_Backward', 'Rel_Start':'Duration', 'Bits/s_Forward':'Bits/s_Backward'} 

    #setting green o's for normal and red x's for botnets
    palette = {'Normal':'#32AB60', 'Botnet':'#DB4052'} 
    markers = {'Normal':'o', 'Botnet':'X'}

    #iterating through each key value combo in the axis dictionary seting the key as the x-axis and value as the y-axis
    for x, y in axis.items():
        x_axis = x.replace('_', ' ')
        y_axis = y.replace('_', ' ')

        plt.figure(figsize = (12, 8)) #set the graph as 12 by 8 pixels
        #graph the iterated x, y pair as a scatter plot and distinguish them based on the predictions
        sns.scatterplot(data = data, x = x, y = y, hue = 'Data', style = 'Data', s = 200, palette = palette, markers = markers) 

        plt.title(f'{x_axis} to {y_axis}', fontsize = 22) # set the title as x to y as defined and its font size
        #set the x and y labels font size
        plt.xlabel(f'{x_axis}', fontsize = 15) 
        plt.ylabel(f'{y_axis}', fontsize = 15)
        #set a balck horizontal and vertical line at point 0
        plt.axvline(0, color = 'black')
        plt.axhline(0, color = 'black')
        plt.legend() #display the legend
    #return all the 6 plots after they have all been analysed
    plt.show()