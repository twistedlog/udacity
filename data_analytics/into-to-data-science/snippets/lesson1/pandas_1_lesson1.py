import pandas as pd

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
