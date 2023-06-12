 elif (f[char] == '('): 
 	counter = 1
 	i = char + 1

 	partial_function = f[i:(len(f) - 1)]
 	parentheses_function_return = find_complete_parentheses(partial_function)
 	counter = counter + parentheses_function_return[0][0]
 	first_parentheses = parentheses_function_return[0][1]
 	char += counter

 	# First parentheses is finished
 	# Check for '/'
 	if (char != (len(f) - 1)):
 		if (f[char + 1] == '/'):
	 		# First, check if there is a '(' after
	 		# The denominator is in parentheses
	 		if (f[char + 2] == '('):
				parentheses_function_return_two = find_complete_parentheses(f[(char + 3):(len(f))])
				counter += parentheses_function_return_two[0][0]
	 			second_parentheses = parentheses_function_return_two[0][1]
	 			char += counter
	 			final_first_parentheses = function_to_display_helper(first_parentheses)
	 			final_second_parentheses = function_to_display_helper(second_parentheses)
	 			str_list.append(r' \frac{')
	 			str_list.append(final_first_parentheses)
	 			str_list.append(r'}{')
	 			str_list.append(final_second_parentheses)
	 			str_list.append(r'}')
	 		# Else, the denominator is just one number
	 		else:
	 			# final_first_parentheses = helper function first_parentheses
	 			final_first_parentheses = function_to_display_helper(first_parentheses)
	 			# append it all to str_list
	 			denominator = f[char + 2]
	 			str_list.append(r' \frac{')
	 			str_list.append(final_first_parentheses)
	 			str_list.append(r'{')
	 			str_list.append(denominator)
	 			str_list.append(r'}')
	 	# No fraction
	 	else:
	 		final_first_parentheses = function_to_display_helper(first_parentheses)
	 		str_list.append(r'{(')
	 		str_list.append(final_first_parentheses)
	 		str_list.append(')}')
 	else:
 		final_first_parentheses = function_to_display_helper(first_parentheses)
        str_list.append(r'{')
        str_list.append(final_first_parentheses)
        str_list.append('}')
 		break
	 	