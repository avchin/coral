"""
Adeline Chin
Section AC
This file contains the functions for cleaning the data sets
containing coral data.
"""
import pandas as pd


def clean_dongsha_df(dongsha):
    '''
    Reads in a dataset of coral information for Dongsha, China.
    Returns a dataframe of the calcification rates for each coral
    site for the years 1953 to 2013.
    '''
    dongsha.replace({'                nd': -1})
    ids = dongsha['core_id'].unique()
    id_df = dict()
    for id in ids:
        rates = dongsha[dongsha['core_id'] == id]
        id_df[id] = rates['calcification_rate'].tolist()
    dongsha = pd.DataFrame.from_dict(id_df)
    return dongsha


def clean_dongsha_status(dongsha):
    '''
    Reads in the dataset for coral information in Dongsha, China.
    Returns a dataframe matching each coral site to its status.
    '''
    df = dongsha[["core_id", "status_July_2015"]]
    df = df.drop_duplicates()
    df = df.set_index('core_id')
    return df


def clean_dongsha_stressbands(dongsha, dongsha_status):
    data = dongsha[['core_id', 'stress_bands']]
    data = data.drop_duplicates()
    data = data.set_index('core_id')
    df = pd.concat([data, dongsha_status], axis=1)
    df = df.replace({"              none": 0})
    df = df.replace({"  alive;_pigmented": 0})
    df = df.replace({"          bleached": 1})
    df = df.replace({"              dead": 2})
    return df
