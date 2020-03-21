import numpy as np
import matplotlib.pyplot as plt

#arrays
a = np.array([1, 2, 3])
print (type(a), a.shape, a[0], a[1], a[2])
a[0] = 5 
print (a)

#2d array
b = np.array([[1, 2, 3],[4,5,6]])
print (b)
print  (b.shape)
print (b[0, 0], b[0, 1], b [1, 0])

#matplotlib
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
