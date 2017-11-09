import json
import matplotlib.pyplot as plt
from numpy.random import rand

algorithm = input('Which Algorithm?  ')


with open("converge_steps_" + algorithm) as data_file:    
	converge_steps = json.load(data_file)
with open("converge_points_" + algorithm) as data_file:    
	converge_points = json.load(data_file)

min = 10000
max = -10000
for i in range(101) :
	for j in range(101) :
		if converge_steps[i][j] > max :
			max = converge_steps[i][j]
		if converge_steps[i][j] != -1 and converge_steps[i][j] < min :
			min = converge_steps[i][j]



x_stars = [[0,1],[1,0],[0,-1],[-1,0],[0,0]]
tolerance = 0.001
def converge_to_global_min(point):
	x = point[0]
	y = point[1]
	converge = False
	for x_star in x_stars :
		if x > x_star[0] - tolerance and x < x_star[0] + tolerance and y > x_star[1] - tolerance and y < x_star[1] + tolerance :
			converge = True
	return converge


fig, ax = plt.subplots()
for i in range(101) :
	for j in range (101):
		if converge_points[i][j] == []:
			continue
		x = -2+0.04*i
		y = -2+0.04*j
		if converge_to_global_min(converge_points[i][j]) :
			color = "g"
		else : 
			color = "r"
		#print(color)
		ax.scatter(x, y,  c = color, s = 10,
               alpha=1, edgecolors='none')
ax.legend()
ax.grid(False)
plt.show()


