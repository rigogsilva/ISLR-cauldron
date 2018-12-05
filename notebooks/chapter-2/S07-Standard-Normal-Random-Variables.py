import cauldron as cd

import numpy as np

cd.display.head('Creates random Matrix')

x = np.random.standard_normal(50)
print('Standard normal:')
print(x)

mean = 50
standard_deviation = .1
y = np.random.normal(mean, standard_deviation, 50)
print('\nNormal (mean: 50, std: 0.1):')
print(y)
print('actual mean:', y.mean())
print('actual std:', y.std())

correlation = np.correlate(x, y)
print('\nCorrelation:')
print(correlation)
