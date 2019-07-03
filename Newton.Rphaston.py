import numpy as np
def f(x):
	return x**4 - 10*x**3 + 3*x**2 + x + 23
def df(x):
	return 4 * x**3 + 30*x**2 + 6*x + 1
a = 1
b = 1
for inter in range (1,3):
	c = a - f(a) / df(a)
	a = c
	print("Su Interaccion es de ",b,"raiz ",a)
	b +=1


	
