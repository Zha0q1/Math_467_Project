import json
import matplotlib.pyplot as plt
from numpy.random import rand

algorithm = input('Which Algorithm?  ')


with open("converge_steps_" + algorithm) as data_file:    
	converge_steps = json.load(data_file)
with open("converge_points_" + algorithm) as data_file:    
	converge_points = json.load(data_file)

fig, ax = plt.subplots()
for i in range(101) :
	for j in range (101):
		if converge_points[i][j] == []:
			continue
		x = converge_points[i][j][0]
		y = converge_points[i][j][1]
		color = (0,0,0)
		#print(color)
		ax.scatter(x, y,  c = color, s = 10,
               alpha=0.04, edgecolors='blue')
ax.legend()
ax.grid(False)
plt.show()


