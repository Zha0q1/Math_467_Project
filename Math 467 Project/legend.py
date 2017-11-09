import json
import matplotlib.pyplot as plt
from numpy.random import rand

fig, ax = plt.subplots()
for i in range(101) :
	x = 1+0.02*i
	y = 0
	color = (float(i)/100, 1-float(i)/100,0)
	ax.scatter(x, y,  c = color, s = 200,
               alpha=1)
ax.legend()
ax.grid(False)
plt.show()


