# -*- coding: utf-8 -*-
"""
Created on Sat May 17 20:22:16 2014

@author: yosukesugishita
"""

# Split projects.csv into train.csv and submit.csv

import pandas as pd
import os
import numpy as np

this_filepath = os.path.realpath(__file__)
home_dir = os.path.dirname(os.path.dirname(this_filepath))

#filepath = home_dir + "/data/small/projects_h1000.csv" # for testing
filepath = home_dir + "/data/original/projects.csv"
dat = pd.read_csv(filepath)

slice_index = np.where(dat.date_posted=='2013-12-31')[0][0]
submit = dat.iloc[0:slice_index,]
train = dat.iloc[slice_index:, ]
submit = submit.sort('projectid', ascending=False) # need to sort this for submission later
