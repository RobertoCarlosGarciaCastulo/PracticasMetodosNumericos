import numpy as np
def f(x):
	return x**4 - 10*x**3 + 3*x**2 + x + 23
def df(x):
	return 4 * x**3 + 30*x**2 + 6*x + 1
a = 1
b = 2
error = ((f(a) - f(a+1))/ f(a))

while error < 0.0000000:
	a = a - f(a) / df(a)
	c = a
	print("Su Interaccion es de ",b,"raiz ",c)
	b +=1


	
