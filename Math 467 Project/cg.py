import numpy as np
import numdifftools as nd
from copy import deepcopy
import json


Q = [[3,0,1],[0,4,2],[1,2,3]]
b = [3,0,1]
fun = lambda x: 0.5 * np.dot( np.dot(x,Q) , x) - np.dot(b,x)

fun = lambda x: (x[0]**4 + x[1]**4 - 6 * x[0]**2 * x[1]**2 - 1)**2 + (4 * x[0]**3 * x[1] - 4 * x[0] * x[1]**3)**2
gradient = nd.Gradient(fun)
hessian = nd.Hessian(fun)


x0 = 0
x1 = 0.01
uncert = 0.0001
def secant_method(phi) :
	#print("secant")
	i = 0
	x_old = x0
	x_cur = x1
	gradient2 = nd.Gradient(phi)
	while True :
		#print("dd")
		#print(x_cur)
		#print(x_old)
		if i == 100 or abs(gradient2(x_cur)-gradient2(x_old)) <= abs(gradient2(x_old)) * uncert :
			return x_cur
		x_new = (gradient2(x_cur) * x_old - gradient2(x_old) * x_cur) / (gradient2(x_cur) - gradient2(x_old))
		x_old = deepcopy(x_cur)
		x_cur = deepcopy(x_new)
		i += 1


alpha0 = 1
tau = 0.5
epsil = 0.3
def backtracking(x,d) :
	alpha = alpha0
	while True :
		#print('________________')
		left = fun(x+alpha*d)
		right = fun(x) + epsil * alpha * np.dot(d, gradient(x))
		#print(left)
		#print(right)
		if left <= right :
			return alpha
		alpha *= tau



epsilon = 0.0001
def conjugate_gradient(x,it_count) :
	g = gradient(x)
	d = -g
	x_old = [100,100]
	while True :
		#print(it_count)

		#print(x_old)
		#print(x)
		#print(d)
		if np.linalg.norm(np.subtract(x_old,x)) <= max(np.linalg.norm(x_old),1) * epsilon :
			return [x[0],x[1]], it_count
		if it_count == 999 :
			return [x[0],x[1]], -1
		x0 = x
		dn = d / np.linalg.norm(d)
		phi = lambda x: fun(x0 + x * dn)
		#alpha = - np.dot(g,d)/np.dot( np.dot(d,hessian(x)) , d) 
		#print(dn)
		#alpha = secant_method(phi)	
		
		alpha = backtracking(x,dn)
		#print(alpha)	
		x_old = deepcopy(x)
		x = x + alpha * dn
		g_next = gradient(x)
		beta = np.dot(g_next,g_next) / (np.dot(g,g))
		g = deepcopy(g_next)
		d = -g + beta * d
		it_count += 1
		if it_count%4 == 0:
			d = -g
		
'''
x_star, it_count = conjugate_gradient([-1.8836,0.025],0)
print(x_star)
print(it_count)


'''
with open("converge_steps_cg") as data_file:    
	converge_steps = json.load(data_file)
with open("converge_points_cg") as data_file:    
	converge_points = json.load(data_file)

for i in range (90,101) :
	print("processing " + str(i) + "%")
	for j in range (101): 
		print(j)
		if i == 50 and j == 50 :
			continue
		converge_points[i][j], converge_steps[i][j] = conjugate_gradient([-2+0.04*i,-2+0.04*j],0)

print("success!")

in_json = json.dumps(converge_steps)
file_object = open('converge_steps_cg', 'w')
file_object.write(in_json)
file_object.close( )

in_json = json.dumps(converge_points)
file_object = open('converge_points_cg', 'w')
file_object.write(in_json)
file_object.close( )

