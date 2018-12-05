import cauldron as cd
import matplotlib.pyplot as plt
import numpy as np

cd.display.head('\nContour plot:')
x = np.arange(1, 11)
y = x

X, Y = np.meshgrid(x, y)


def f(x, y):
    """
    :param x:
        x from np.meshgrid
    :param y:
        y from np.meshgrid
    """
    return np.cos(y)/(1 + x**2)


Z = f(X, Y)
CS = plt.contour(X, Y, Z)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Contour plot')
cd.display.pyplot()
