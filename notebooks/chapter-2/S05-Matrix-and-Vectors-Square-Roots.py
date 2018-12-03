import cauldron as cd
import numpy as np

cd.display.head('Getting square root of a matrix or a vector')

matrix = cd.shared.matrix

cd.display.text('Matrix:')
print(matrix)

cd.display.text('Sqrt of Matrix:')
sqrt_root = np.sqrt(matrix)
print(sqrt_root)
