import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], linewidths=0.2)
    

    # Create first line of best fit
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = range(1880, 2051)
    ax.plot(x1, res1.slope * x1 + res1.intercept, color='orange', linewidth=2)

    # Create second line of best fit
    df_recent = df.loc[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051)
    ax.plot(x2, res2.slope * x2 + res2.intercept, color='red', linewidth=2)

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()