def Divi(a,b):
	while True:
		try:
			return a/b

		except ZeroDivisionError:
			print (" Ops! No era valido. Intente nuevemente")
			break 
		except TypeError:
			print ("Error, No se permiten letras solo numeros")
			break 
print(Divi('a',0))

