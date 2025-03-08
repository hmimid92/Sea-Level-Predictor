import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv');
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='original data');

    # make predictions
    b1, b0, r_value, p_value, std_err  = linregress(df['Year'], df['CSIRO Adjusted Sea Level']);
    years_extended = np.arange(1880, 2051, 1);
    line = [b1*xi + b0 for xi in years_extended]
    dff=df.copy();
    dff = dff[dff['Year'] >= 2000];
    b11, b00, r_value1, p_value1, std_err1  = linregress(dff['Year'], dff['CSIRO Adjusted Sea Level']);
    years_extended2 = np.arange(2000, 2051, 1);
    line2 = [b11*xi + b00 for xi in years_extended2]
    # Create first line of best fit
    plt.plot(years_extended, line, 'r', label='fitted line');

    # Create second line of best fit
    plt.plot(years_extended2, line2, 'g', label='from 2000');
    
    # Add labels and title
    plt.legend();
    plt.xlabel('Year');
    plt.ylabel('Sea Level (inches)');
    plt.title('Rise in Sea Level'); 
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png');
    return plt.gca();