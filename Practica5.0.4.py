def agregar_una_vez(lista,el):
	while True:
		try:
			if el in lista:
				raise ValueError
			else:
				lista.append(el)
			return el 
		except ValueError:
			print("Error",[el])
			break
print(agregar_una_vez([1],1))

