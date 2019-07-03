while True:
	try: 
		colores = { 'rojo':'red', 'verde':'green','negro':'black'}
		colores['blanco']
	except KeyError:
		print (" Ops! No es valido. Intente nuevemente")
		break 
