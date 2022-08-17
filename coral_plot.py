"""
Adeline Chin
Section AC
This file contains the functions that plot calcification
rates, water pH, and water temperature.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import spearmanr


def plot_calcification_rates(calcif_rates):
    '''
    Reads in a dataset for calcification rates of the coral at
    Dongsha Atoll.
    Plots a line plot of the calcification rate from the years
    1954 to 2012.
    '''
    x = calcif_rates['year']
    y = calcif_rates['Calcif_rate']
    coef = np.polyfit(x, y, 1)
    poly1d_fn = np.poly1d(coef)
    plt.plot(x, y, 'yo', x, poly1d_fn(x), '--k')
    plt.ylim(0.0, 3.0)
    plt.ylabel('Calcification Rate')
    plt.title('Calcification Rates 1954-2012')
    plt.savefig('Calcification Rates 1954-2012', bbox_inches='tight')


def temp_pH_relation(ph_temp):
    '''
    Reads in pH and temperature data for water at McMurdo Sound, Antarctica.
    Plots line graphs comparing the change of pH and the change
    of water temperature over time.
    '''
    ph_temp.plot(x='               time', y='              pH', kind='line')
    plt.xticks(fontsize=10, rotation=45)
    plt.ylabel('pH')
    plt.savefig('pH over time', bbox_inches='tight')
    ph_temp.plot(x='               time', y=' temp', kind='line')
    plt.xticks(fontsize=10, rotation=45)
    plt.ylabel('temp')
    plt.savefig('temp over time', bbox_inches='tight')
    data1 = ph_temp['              pH']
    data2 = ph_temp[' temp']
    corr, _ = spearmanr(data1, data2)
    print('Spearmans correlation: %.3f' % corr)
