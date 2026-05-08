import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,100,1000)
print(x)
y = np.sin(x)
print(y)
plt.plot(x,y)

plt.plot(x,y)
plt.title("grafica de seno")
plt.show()