import cauldron as cd
import numpy as np
import matplotlib.pyplot as plt

x = np.random.standard_normal(100)
y = np.random.standard_normal(100)

plt.plot(
    x, '-', lw=2, color='red'
)
plt.plot(
    y, '-', lw=2, color='blue'
)

plt.xlabel('This is the x-axis')
plt.ylabel('This is the y-axis')
plt.title('Plot of X vs Y')

cd.display.pyplot()
