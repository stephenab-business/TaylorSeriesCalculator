def find_complete_parentheses(sliced_function):
	return_list = []
	more_parentheses = 0
	counter = 0
	first_parentheses = ''
	i = 0
 	while i < len(sliced_function):
 		# If whitespace skip
 		if (sliced_function[i] == ' '):
 			i += 1
 			counter += 1
 			continue
 		# Else if (, add to counter
 		elif (sliced_function[i] == '('):
 			more_parentheses += 1
 			i += 1
 			counter += 1
 			continue
 		# Else if )
 		elif (sliced_function[i] == ')'):
 			# Check counter
 			if (more_parentheses > 0):
 				i += 1
 				counter += 1
 				more_parentheses -= 1
 				continue
 			# Else it is the actual last ')'
 			else:
 				# First parentheses value
 				first_parentheses = sliced_function[0:i]
 		# Else normal number or symbol
 		else:
 			i += 1
 			counter += 1
 			continue
 		break
 	return_list.append((counter, first_parentheses))
 	return return_list