"""
Adeline Chin
Section AC
This file contains the machine learning functions and
correlation calculation functions.
"""
import pandas as pd
import numpy as np
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from scipy.stats import spearmanr


def nstressband_correlation(stressbands):
    '''
    Calculates the Spearmans correlation of the number of
    stressbands a coral has had and whether the coral is alive,
    bleached, or dead.
    '''
    df = stressbands.replace({"  1983;_1998;_2007": 3})
    df = df.replace({"2007": 1})
    df = df.replace({"1998": 1})
    df = df.replace({"        1998;_2007": 2})
    covariance = np.cov(df["stress_bands"],
                        df["status_July_2015"])
    print(covariance)
    corr, _ = spearmanr(df["stress_bands"],
                        df["status_July_2015"])
    print('Spearmans correlation: %.3f' % corr)


def mean_stressband_correlation(stressbands):
    '''
    Calculates the Spearmans correlation of the mean years
    between stressbands for a coral and whether the coral is alive,
    bleached, or dead.
    '''
    df = stressbands.replace({"  1983;_1998;_2007": 12})
    df = df.replace({"2007": 0})
    df = df.replace({"1998": 0})
    df = df.replace({"        1998;_2007": 9})
    covariance = np.cov(df["stress_bands"],
                        df["status_July_2015"])
    print(covariance)
    corr, _ = spearmanr(df["stress_bands"],
                        df["status_July_2015"])
    print('Spearmans correlation: %.3f' % corr)


def stressband_predict(stressbands):
    '''
    Predicts the status of a coral based on the number of
    stressbands.
    '''
    df = stressbands.replace({"  1983;_1998;_2007": 3})
    df = df.replace({"2007": 1})
    df = df.replace({"1998": 1})
    df = df.replace({"        1998;_2007": 2})
    features = df.columns.tolist()
    features.remove('status_July_2015')
    df[features] = df[features].astype(float)
    encoder = OrdinalEncoder()
    d_encoded = encoder.fit_transform(df[features])
    data_encoded = pd.DataFrame(d_encoded, columns=features)
    encoder = LabelEncoder()
    target_encoded = encoder.fit_transform(df['status_July_2015'])
    data_encoded['status_July_2015'] = target_encoded
    encoder.inverse_transform(target_encoded)
    features_train, features_test, labels_train, labels_test = \
        train_test_split(df.drop('status_July_2015', axis=1),
                         data_encoded['status_July_2015'],
                         stratify=data_encoded['status_July_2015'],
                         test_size=0.5)
    cnb = CategoricalNB(min_categories=df.columns.nunique())
    cnb.fit(features_train, labels_train)
    train_predictions = cnb.predict(features_train)
    print('Train Accuracy:', accuracy_score(labels_train, train_predictions))
    test_predictions = cnb.predict(features_test)
    print('Test Accuracy:', accuracy_score(labels_test, test_predictions))


def coral_predict(dongsha_df, dongsha_status):
    '''
    Predicts the status of a coral based on its historic
    calcification rate.
    '''
    dongsha_df = dongsha_df.transpose()
    data = pd.concat([dongsha_df, dongsha_status], axis=1)
    columns = []
    columns.extend(range(1953, 2014))
    columns.append('status')
    data.set_axis(columns, axis=1, inplace=True)
    data = data.replace({"                nd": 0})
    features = data.columns.tolist()
    features.remove('status')
    data[features] = data[features].astype(float)
    encoder = OrdinalEncoder()
    d_encoded = encoder.fit_transform(data[features])
    data_encoded = pd.DataFrame(d_encoded, columns=features)
    encoder = LabelEncoder()
    target_encoded = encoder.fit_transform(data['status'])
    data_encoded['status'] = target_encoded
    encoder.inverse_transform(target_encoded)
    features_train, features_test, labels_train, labels_test = \
        train_test_split(data.drop('status', axis=1), data_encoded['status'],
                         stratify=data_encoded['status'], test_size=0.5)
    cnb = CategoricalNB(min_categories=data.columns.nunique())
    cnb.fit(features_train, labels_train)
    train_predictions = cnb.predict(features_train)
    print('Train Accuracy:', accuracy_score(labels_train, train_predictions))
    test_predictions = cnb.predict(features_test)
    print('Test Accuracy:', accuracy_score(labels_test, test_predictions))
