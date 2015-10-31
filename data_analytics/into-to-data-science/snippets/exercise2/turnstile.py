import numpy as np
import csv


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
                _writeline(f_out, _readline(line))


def _readline(line):
    prefix = np.array(line[:3])
    line = np.array([ele.strip() for ele in line[3:]])
    split_factor = len(line) / 5
    splits = np.split(line, split_factor)
    print splits
    for split in splits:
        return np.concatenate((prefix, split), axis=1).tolist()


def _writeline(f_out, line):
    writer = csv.writer(f_out, delimiter=',')
    writer.writerow(line)


if __name__ == "__main__":
    fix_turnstile_data(['turnstile_110528.txt'])
