while True:
	try:
		lista=[1,2,3,4,5]
		print(lista[10])
	except IndexError:
		print (" Ops! No era valido. Intente nuevemente")
		break 
