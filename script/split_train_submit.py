"""
Created on Sat May 17 20:22:16 2014

@author: yosukesugishita
"""
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

## Split projects.csv into train.csv and submit.csv
import pandas as pd
import numpy as np

filepath = "../data/original/projects.csv"
dat = pd.read_csv(filepath)

slice_index = np.where(dat.date_posted=='2013-12-31')[0][0]
submit = dat.iloc[0:slice_index,]
train = dat.iloc[slice_index:, ]

submit = submit.sort('projectid', ascending=False) # need to sort this for submission later

submit.to_csv("../data/intermediate/submit.csv", index=False)
train.to_csv("../data/intermediate/train.csv", index=False)
