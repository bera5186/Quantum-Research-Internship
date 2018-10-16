import math
import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D
from gd import gradient_descent, func
from matplotlib import animation



fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(-1.5, 1.5, 50)
y = np.linspace(-1.5, 1.5, 50)

X, Y = np.meshgrid(x, y)
zs = np.array([func(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')

x0 = max(x)
y0 = max(y)
learning_rate = 2
epoch = 500

x_gd, y_gd, z_gd = gradient_descent(x0, y0, learning_rate, epoch)


min_point = np.array([max(x), max(y)])
min_point_ = min_point[:, np.newaxis]
ax.plot(*min_point_, func(*min_point_), 'r*', markersize=10)
ax.set_title('surface')
ax.plot(x_gd, y_gd, 'go')
'''for i in range(1, epoch+1):
    ax.annotate('', xy=(x_gd[i], y_gd[i]), xytext=(x_gd[i-1], y_gd[i-1]),
                   arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},
                   va='center', ha='center')
some = list(zs)
#print(some.index(min(some)))
#print(some[2210])'''
plt.show()