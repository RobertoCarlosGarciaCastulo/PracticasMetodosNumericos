import numpy as np 
def f(x):
	return x - np.sin(x)
a = -1
b = 1
error = 0.4
while error > 1e-8:
	c = (a + b) / 2
	fa = f(a)
	fb = f(b)
	fc = f(c)
	if fc == 0:
		raiz = c
	elif fa * fc < 0:
		a = c
	elif fb * fc < 0:
		b = c
	raiz = c
	error = abs(fc)
	
print("Su raiz es ",raiz)
