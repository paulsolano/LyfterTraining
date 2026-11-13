def generate_list_trios(list_a, list_b, list_c): # O(n^3)
	result_list = []
	for element_a in list_a: # O(n)
		for element_b in list_b: # O(n)
			for element_c in list_c: # O(n)
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 