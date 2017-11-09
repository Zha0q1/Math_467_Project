import matplotlib.pyplot as plt
from numpy.random import rand



fig, ax = plt.subplots()
for i in range (11) :
	for j in range (11):
		x = -2+0.4*i
		y = -2+0.4*j
		ax.scatter(x, y,  c = ("#%02X" % int((x+2)/999*255) + '0000' ), 
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)
plt.show()