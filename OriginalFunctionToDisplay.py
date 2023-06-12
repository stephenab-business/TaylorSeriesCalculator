# NOTE: Need to fix if there is a fraction in exponent
# NOTE: Need to fix if there is a double parentheses, '(('
# Function to display function using latex
def function_to_display(f):
    str_list = []
    char = 0
    while char < len(f):
        # If symbol in string is **
        if (f[char] == '*' and f[char + 1] == '*'):
            str_list.append('^')
            char += 1      
        # If symbol in string is *
        elif (f[char] == '*' and f[char + 1] != '*'):
            str_list.append(r' \cdot ')
        elif (f[char] == ' '):
            char += 1
            continue
        elif (f[char] == '/'):
            # Add fraction to list
            str_list.append(r' \frac')
            # Numerator
            if (f[char - 1] == ')'): # There is a parentheses
                current_point_in_list = len(str_list) - 1
                while current_point_in_list >= 0:
                    # Find index for {
                    if (str_list[current_point_in_list] == '{'):
                        first_index = current_point_in_list
                    # Find index for }
                    elif (str_list[current_point_in_list] == '}'):
                        last_index = current_point_in_list
                    current_point_in_list -= 1
                # Slice list from { to }
                numerator = str_list[first_index: last_index + 1]
                # Delete slice from list
                del str_list[first_index: last_index + 1]
                # Add each element onto end of list
                for item in numerator:
                    str_list.append(item)
            else: # There is no parentheses
                del str_list[len(str_list) - 2]
                str_list.append('{')
                str_list.append(f[char - 1])
                str_list.append('}')
            # Denominator
            char += 1 # Character after division symbol
            if (f[char] == '('): # There is a parentheses
                str_list.append('{')
                char += 1
                while char < len(f):
                    if (f[char] == ')'): # End of parentheses found
                        str_list.append('}')
                        break
                    else: # Continue searching
                        str_list.append(f[char])
                        char += 1
            else: # There is no parentheses
                str_list.append('{')
                str_list.append(f[char])
                str_list.append('}')
                char += 1
        elif (f[char] == '('):
            str_list.append('{')
        elif (f[char] == ')'):
            str_list.append('}')
        else:
            str_list.append(f[char])
        char += 1
        
    function = ''.join(str_list)
    # The function I use here is used many times throughout my program. This is a Latex function,
    # which also uses the Math package, and will print out the mathematical values and expressions
    # in a more impressive fashion, rather than printing them out normally.
    display(Math(r'$f(x)={}$'.format(function)))