import cauldron as cd
import numpy as np

cd.display.head('Adding two vectors')
x = np.array([1, 6, 2])
y = np.array([1, 4, 3])

print(f'x length is: {len(x)}')
print(f'y length is: {len(y)}')

cd.display.text('Add x + y')
print(x + y)

# Shared variables globally.
cd.shared.put(
    x=x,
    y=y
)
