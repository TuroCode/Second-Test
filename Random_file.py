import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,10,0.01)
y=x**3

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

