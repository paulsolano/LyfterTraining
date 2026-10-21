def print_10_or_less_elements(list_to_print): # O(1)
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)): # O(1) porque el rango máximo es 10, sin importar el tamaño de la lista
		print(list_to_print[index])