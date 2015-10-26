import pandas as pd
import numpy as np


if True:
    series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -3978628])
    print series

if True:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curicullum Manager',
                              'Course Number', 'Power Level'])
    print series
    print ""
    print series['Instructor']
    print series['Course Number']
    print ""

'''
use boolean operators to select specific items from the series
'''
if True:
    series = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig', 'Puppy', 'kitten'])

    print series > 3
    print ""
    print series[series>3]
    print ""

'''
Data Frames in pandas
'''
if True:
    data = {
        'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]
    }
    football = pd.DataFrame(data)
    print football
    print ""

'''
Pandas also has various functions to help understand some basic information about the data.
1) dtypes: to get the datatype for each column
2) describe: useful for seeing basic statistics of dataframe's numeric columns.
3) head: displays the first five rows of the dataset
4) tail: displays the last five rows of the dataset
'''
if True:
    data = {
        'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]
    }
    football = pd.DataFrame(data)
    print football.dtypes
    print ""
    print football.describe(include='all')
    print ""
    print football.head()
    print ""
    print football.tail()
    print ""
    print football['year']
    print ""
    print football.year  # shorthand for football['year']
    print ""
    print football[['year', 'wins', 'losses']]
    print ""
    # Row selection can be done by follwoing methods:
    # 1) Slicing
    # 2) An individual index (through the functions iloc or loc)
    # 3) Boolean indexing
    print football.iloc[[0]]
    print ""
    print football.loc[[0]]
    print ""
    print football[3:5]
    print ""
    print football[football.wins > 10]
    print ""
    print football[(football.wins > 10) & (football.team == 'Packers')]
