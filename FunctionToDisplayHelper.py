def function_to_display_helper(f):
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
        # If symbol is just whitespace
        elif (f[char] == ' '):
            char += 1
            continue
        
        ## INSERT HERE ##

        # If symbol is an ending parentheses
        elif (f[char] == ')'):
            str_list.append('}')

        # If next symbol is division, make a fraction
        elif(f[char + 1] == '/'):
            str_list.append(r' \frac{')
            str_list.append(f[char])
            str_list.append(r'}{')
            str_list.append(f[char + 2])
            str_list.append(r'}')
            char += 2
            continue
        
        # Else it is just a number, +, or -
        else:
            str_list.append(f[char])
        char += 1
        
    function = ''.join(str_list)
    return function