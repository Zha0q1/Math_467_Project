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

print(hessian([0,0]))




x = [0,0]
print("Gradient and Hessian near point (" + str(x[0]) + "," + str(x[1]) + ")")
print("point: (" + str(x[0]) + "," + str(x[1]+0.01) + ")")
print( gradient([x[0],x[1]+0.01]) )
print(hessian([x[0],x[1]+0.01]) )

print("point: (" + str(x[0]) + "," + str(x[1]-0.01) + ")")
print( gradient([x[0],x[1]-0.01]) )
print(hessian([x[0],x[1]-0.01]) )

print("point: (" + str(x[0]+0.01) + "," + str(x[1]) + ")")
print( gradient([x[0]+0.01,x[1]]) )
print(hessian([x[0]+0.01,x[1]]) )

print("point: (" + str(x[0]-0.01) + "," + str(x[1]) + ")")
print( gradient([x[0]-0.01,x[1]]) )
print(hessian([x[0]-0.01,x[1]]) )

print(gradient([2,2]))

print(gradient([-2,2]))
