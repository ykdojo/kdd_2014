## This file labels the train.csv file with is_exciting
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

import csv
import pandas as pd

# dictinoary of projects
# format: {project_id: is_exciting}
# example: {'ff9d06845bb51a9ee749adc6c0fcbf6a': 'f'} #'f' for false, 't' for true
proj_dict = {}
with open('../data/original/outcomes.csv', 'rb') as f:
    r = csv.reader(f)
    header = next(r)
    for row in r:
        proj_dict[row[0]] = row[1]

train = pd.read_csv('../data/intermediate/train.csv')
train['is_exciting'] = train.projectid.map(lambda x: proj_dict[x])
train.to_csv("../data/intermediate/train_labeled.csv", index=False)
