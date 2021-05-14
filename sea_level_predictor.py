#%%
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
#%%
def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', index_col=0)
    # Create scatter plot
    plt.scatter(
    x=df.index,
    y=df['CSIRO Adjusted Sea Level']
    )

    # Create first line of best fit
    linear_reg = linregress(df.index, df['CSIRO Adjusted Sea Level'])
    df['lin_1'] = linear_reg.intercept+ linear_reg.slope* df.index
    
    plt.plot(
    range(1880, 2051),
    linear_reg.slope*range(1880, 2051) + linear_reg.intercept,
    color='red'
    )
    # Create second line of best fit
    df_since_2000 = df[
    df.index >= 2000
    ] 
    linear_reg_2 = linregress(df_since_2000.index, df_since_2000['CSIRO Adjusted Sea Level'])       
    plt.plot(
    range(2000, 2051),
    linear_reg_2.slope*range(2000, 2051) + linear_reg_2.intercept,
    color='green'
    )
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()