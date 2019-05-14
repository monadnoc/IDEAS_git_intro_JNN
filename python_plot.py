import numpy as np
import matplotlib.pyplot as plt

l = 314
x = np.linspace(0, 2*np.pi, num=l)
y = np.copy(x)
plt.plot(x, y)
plt.show()
