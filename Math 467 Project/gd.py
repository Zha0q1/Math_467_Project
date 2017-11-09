import numpy as np
import numdifftools as nd
from copy import deepcopy
import json

fun = lambda x: (x[0]**4 + x[1]**4 - 6*x[0]**2*x[1]**2 - 1)**2 + (4*x[0]**3*x[1] - 4*x[0]*x[1]**3)**2



gradient = nd.Gradient(fun)
hessian = nd.Hessian(fun)


alpha = 0.02
step = 0.02
epsilon = 0.001
def gradient_descent(x,it_count):
	x_old = [99,99]
	while (True) :
		#print(x)
		if np.linalg.norm(np.subtract(x, x_old)) <= max(np.linalg.norm(x_old),1) * epsilon:
			return [x[0],x[1]], it_count
		if it_count == 999 :
			return [x[0],x[1]], -1

		grad = gradient(x)

		x_old = deepcopy(x)
		progression = alpha * grad
		if np.linalg.norm(progression) > step:
			progression = progression / np.linalg.norm(progression) * step
		x -= progression
		it_count += 1

'''
converge_steps = [[-1 for i in range(101)] for j in range(101)]

x_star, converge_steps[0][0] = gradient_descent([-2,0.24],0)
print(x_star)
print(converge_steps[0][0])


for i in range (1) :
	print("processing " + str(i) + "%")
	for j in range (101): 
		print(j)
		x_star, converge_steps[i][j] = gradient_descent([-2+0.04*i,-2+0.04*j],0)

print(converge_steps[0])
'''


with open("converge_steps_gd") as data_file:    
	converge_steps = json.load(data_file)
with open("converge_points_gd") as data_file:    
	converge_points = json.load(data_file)

for i in range (90,101) :
	print("processing " + str(i) + "%")
	for j in range (101): 
		print(j)
		if i == 50 and j == 50 :
			continue
		converge_points[i][j], converge_steps[i][j] = gradient_descent([-2+0.04*i,-2+0.04*j],0)

#print(converge_points[0])
#print(converge_steps[0])
print("success!")

in_json = json.dumps(converge_steps)
file_object = open('converge_steps_gd', 'w')
file_object.write(in_json)
file_object.close( )

in_json = json.dumps(converge_points)
file_object = open('converge_points_gd', 'w')
file_object.write(in_json)
file_object.close( )



