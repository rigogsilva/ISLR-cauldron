import cauldron as cd

import numpy as np

cd.display.head('Creating a matrix')

matrix = np.matrix([[1, 3], [2, 4]])

print(matrix)

cd.shared.matrix = matrix
