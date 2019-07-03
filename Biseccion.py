import numpy as np 
def f(x):
	return x**4-10*x**3+3*x**2+x+23
a = 9
b = 12
error = 0.4
while error > 1e-12:
	c = (a + b) / 2
	fa = f(a)
	fb = f(b)
	fc = f(c)
	if fc == 0:
		raiz = c
	elif fa * fc < 0:
		b = c
	elif fb * fc < 0:
		a = c
	raiz = c
	error = abs(fc)
	
print("Su raiz es ",raiz)
