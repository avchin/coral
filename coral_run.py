"""
Adeline Chin
Section AC
This file contains the main functions used to run all code.
"""
import pandas as pd
from coral_plot import plot_calcification_rates
from coral_plot import temp_pH_relation
from coral_clean import clean_dongsha_df
from coral_clean import clean_dongsha_status
from coral_clean import clean_dongsha_stressbands
from coral_predict import nstressband_correlation
from coral_predict import mean_stressband_correlation
from coral_predict import stressband_predict
from coral_predict import coral_predict


def main():
    calcif_rates = pd.read_csv("calcif_rates.csv")
    plot_calcification_rates(calcif_rates)
    ph_temp = pd.read_csv('ph_temp.csv')
    temp_pH_relation(ph_temp)
    dongsha = pd.read_csv("Dongsha_calcification.csv")
    dongsha_df = clean_dongsha_df(dongsha)
    dongsha_status = clean_dongsha_status(dongsha)
    stressbands = clean_dongsha_stressbands(dongsha, dongsha_status)
    nstressband_correlation(stressbands)
    mean_stressband_correlation(stressbands)
    stressband_predict(stressbands)
    coral_predict(dongsha_df, dongsha_status)


if __name__ == '__main__':
    main()
