import numpy as np

'''
Numpy arrays are like Python lists except that everything inside a Numpy array should be of same type

'''
if True:
    array = np.array([1, 4, 5, 8], float)
    print array
    print ""
    array = np.array([[1, 2, 3], [4, 5, 6]], float)
    print array

if True:
    array = np.array([1, 4, 5, 8], float)
    print array
    print ""
    print array[1]
    print ""
    print array[:2]
    print ""
    array[1] = 5.0
    print array[1]

if True:
    two_d_array = np.array([[1, 2, 3], [4, 5, 6]], float)
    print two_d_array
    print ""
    print two_d_array[1][1]
    print ""
    print two_d_array[1, :]
    print two_d_array[:, 2]
    print two_d_array[:, 1]

'''
Arithmetic operations that can be done with Numpy
'''

if True:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([4, 5, 6], float)
    print array_1 + array_2
    print ""
    print array_1 - array_2
    print ""
    print array_1 * array_2

if True:
    array_1 = np.array([[1, 2], [3, 4]], float)
    array_2 = np.array([[5, 6], [7, 8]], float)
    print array_1 + array_2
    print ""
    print array_1 - array_2
    print ""
    print array_1 * array_2
