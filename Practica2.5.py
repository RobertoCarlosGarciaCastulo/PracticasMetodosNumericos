#Pedir un numero n...comprabar n es un numero 2.. n>=2 ... generar un contador 
n=0;
i=0;
num=int(input("Dame tu numero "))
while num<1:
	print('Dame un numero que no sea menor a uno')
if num ==  2:
	print(num)
else:
    for n in range (2,num):
		si = True
		for i in range (2, i):
	    	if n % i==0:
	    	    si = False
	    	if si is True:
	 			print(i)
input(" ")
