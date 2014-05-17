# Try making a dictinoary of {project_id -> is_exciting} from outcomes.csv.
# There are around 600,000 projects. --- not sure if it's possible to put them all into memory.

# In [6]: sys.getsizeof(d)
# Out[6]: 280 (bytes)

# -> 280 * 600,000 = 168 MB. -> should fit in memory.

import csv

# list of dictionaries
dict_list = []
#filepath = 'data/small/outcomes_h1000.csv' # use a small file for testing
filepath = 'data/original/outcomes.csv' # this is for real
with open(filepath, 'rb') as f:
    r = csv.reader(f)
    header = next(r)
    for row in r:
        # format: {project_id: is_exciting}
        # example: {'ff9d06845bb51a9ee749adc6c0fcbf6a': 'f'} #'f' for false, 't' for true
        dict_list.append({row[0]: row[1]})
        
print "made " + str(len(dict_list)) + " objects!"