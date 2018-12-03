import cauldron as cd
import numpy as np

cd.display.head('Raise matrix to the power of 2')

matrix = cd.shared.matrix

cd.display.text('Matrix:')
print(matrix)

cd.display.text('Matrix:')
power_of_two = np.power(matrix, 2)
print(power_of_two)
