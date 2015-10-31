import csv
import numpy as np

def fix_turnstile_data(filenames):
    if not(isinstance(filenames, list)):
        raise TypeError

    for filename in filenames:
        process(filename)


def process(filename):
    with open(filename, 'r') as f_in:
        with open('updated_' + filename, 'w') as f_out:
            reader_in = csv.reader(f_in, delimiter=',')
            for line in reader_in:
                _readwriteline(f_out, line)


def _readwriteline(f_out, line):
    line = [ele.strip() for ele in line]
    prefix = np.array(line[:3])
    line = np.array(line[3:])
    split_factor = len(line) / 5
    splits = np.split(line, split_factor)
    #print splits
    for split in splits:
        _writeline(f_out, np.concatenate((prefix, split), axis=1).tolist())



def _writeline(f_out, line):
    #print line
    writer = csv.writer(f_out)
    writer.writerow(line)
