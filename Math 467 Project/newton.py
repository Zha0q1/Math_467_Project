import numpy as np
import numdifftools as nd
from copy import deepcopy
import json

fun = lambda x: (x[0]**4 + x[1]**4 - 6*x[0]**2*x[1]**2 - 1)**2 + (4*x[0]**3*x[1] - 4*x[0]*x[1]**3)**2





gradient = nd.Gradient(fun)
hessian = nd.Hessian(fun)

x_stars = [[0,1],[1,0],[0,-1],[-1,0]]


alpha0 = 1
tau = 0.8
epsil = 0.5
def backtracking(x,d) :
	alpha = alpha0
	#print('________________')
	while True :
		
		left = fun(x+alpha*d)
		right = fun(x) + epsil * alpha * np.dot(d, gradient(x))
		#print(left)
		#print(right)
		if abs(left - right) < 0.1 * abs(right) :
			#print(alpha)
			return alpha
		alpha *= tau


epsilon = 0.0001
def newton(x,it_count):
	x_old = [100,100]
	while True :
		'''
		print('........... ')
		print(x_old)
		print(x)
		print (np.linalg.norm(np.subtract(x_old, x)))
		print (epsilon * np.linalg.norm(x_old))
		'''
		if np.linalg.norm(np.subtract(x_old, x)) <= max(np.linalg.norm(x_old),1) * epsilon:
			return [x[0],x[1]], it_count
		if it_count == 999 :
			return [x[0],x[1]], -1

		grad = gradient(x)
		if np.linalg.norm(grad) == 0 :
			return x, it_count
		hes = hessian([x[0],x[1]])
		try:
			inverse_hes = np.linalg.inv(hes)
		except numpy.linalg.LinAlgError:
			return [x[0],x[1]], -1

		d = np.dot(inverse_hes, grad)
		#d = d / np.linalg.norm(d)
		'''
		if np.linalg.norm(d) > 0.02 :
			alpha = backtracking(x,d)
		else :
			alpha = 1
		'''
		alpha = 1#backtracking(x,d)
	

		x_old = deepcopy(x)
		x -= alpha * d;
		it_count += 1


'''
x_star, it_count = newton([-1.8836,0.025],0)

print(x_star)
print(it_count)


converge_steps = [[-1 for i in range(101)] for j in range(101)]
converge_points = [[[] for i in range(101)] for j in range(101)]
for i in range (1) :
	print("processing " + str(i) + "%")
	for j in range (101): 
		print(j)
		converge_points[i][j], converge_steps[i][j] = newton([-2+0.04*i,-2+0.04*j],0)

print(converge_points[0])
print(converge_steps[0])
'''


with open("converge_steps_nt") as data_file:    
	converge_steps = json.load(data_file)
with open("converge_points_nt") as data_file:    
	converge_points = json.load(data_file)

for i in range (80,101) :
	print("processing " + str(i) + "%")
	for j in range (101): 
		print(j)
		if i == 50 and j == 50 :
			continue
		converge_points[i][j], converge_steps[i][j] = newton([-2+0.04*i,-2+0.04*j],0)

#print(converge_points[0])
#print(converge_steps[0])
print("success!")

in_json = json.dumps(converge_steps)
file_object = open('converge_steps_nt', 'w')
file_object.write(in_json)
file_object.close( )

in_json = json.dumps(converge_points)
file_object = open('converge_points_nt', 'w')
file_object.write(in_json)
file_object.close( )



