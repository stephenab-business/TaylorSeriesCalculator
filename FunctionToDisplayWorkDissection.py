# PROBLEM AT THE BOTTOM: IF COUNTER, COUNTER_TWO, AND COUNTER_THREE ARE SET TO 0, IT WILL BECOME STUCK, REVISE

# Original Part of Conditional Statement



 # If symbol is a parentheses
        elif (f[char] == '('):
            counter = 0
            counterTwo = 0
            counterThree = 0
            counterFour = 0
            amountOfParentheses = 0
            amountOfParenthesesTwo = 0
            
            ## FIRST WHILE LOOP ##

            ## END FIRST WHILE LOOP ##

            # Skip the amount that it took to find the first set of parentheses
            # Only the fraction will execute this part of the code
            char += counter
            # If fraction is found, it will skip the division symbol and skip the next number/set of parentheses attached to fraction
            # only the fraction will execute this part of the code
            char += counterTwo
            # Will denominator if there is no parentheses or will skip the whitespace in denominator
            char += counterThree
            # Will skip denominator if there is parentheses
            char += counterFour






# FIRST WHILE LOOP

            i = char + 1
            # While loop to find ')'
            while i < len(f):
                # If whitespace, skip and continue
                if (f[i] == ' '):
                    i += 1
                    counter += 1 
                    continue
                # If there is another parentheses started
                elif (f[i] == '('):
                    # Find the second ')', not the first
                    # Increment amountOfParentheses, then when checking for ')', must actually subtract from the amount and do it again
                    amountOfParentheses += 1
                    i += 1
                    count += 1
                    continue
                # Found ending parentheses
                elif (f[i] == ')'):
                    
                    ## CODE FOR ')' ##

                    ## END CODE FOR ')' ##

                # Normal number or symbol, must continue until ending parentheses found
                else:
                    i += 1
                    counter += 1
                    continue




# CODE FOR ')'

                    # This is not last parentheses
                    if (amountOfParentheses > 0):
                        i += 1
                        counter += 1
                        amountOfParentheses -= 1
                        continue
                    # This is last parentheses, moving on
                    else:
                        j = i
                        # While Loop to find if next character is '/'
                        while j < len(f):
                            # Whitespace, skip
                            if (f[j] == ' '):
                                j += 1
                                counterTwo += 1
                                continue
                            # Division symbol, so it is a fraction
                            elif (f[j] == '/'):
                                
                                ## FRACTION FOUND ##

                                ## END FRACTION FOUND ##

                            # Normal parentheses, break out of this while loop, which causes previous while loop to break as well
                            else:
                                # Append the normal parentheses
                                # Append normal '('
                                counterTwo = 0
                                counterThree = 0
                                counterFour = 0
                                break
                        break





# CODE FOR FRACTION FOUND

                                # From char to i, numerator
                                numerator = f[i:char]
                                denominator = ''
                                # Recursive call on numerator, stored in a variable
                                final_numerator = function_to_display_helper(numerator)
                                k = j
                                
                                ## NEXT WHILE LOOP ##

                                ## END NEXT WHILE LOOP ##

                                # Denominator finished
                                final_denominator = function_to_display_helper(denominator)
                                # Append the actual fraction string to the list now
                                str_list.append(r' \frac{')
                                str_list.append(final_numerator)
                                str_list.append(r'}{')
                                str_list.append(final_denominator)
                                str_list.append(r'}')



# CODE FOR NEXT WHILE LOOP

                                # While loop
                                while k < len(f):
                                    # If there is whitespace, skip
                                    if (f[k] == ' '):
                                        # increment
                                        k += 1
                                        counterThree += 1
                                    # Check for '(' after the '/'
                                    elif (f[k] == '('):
                                        
                                        ## FINAL WHILE LOOP ##

                                        ## END FINAL WHILE LOOP ##

                                    # Else there is just a number after the '/'
                                    else:
                                        # denominator is next number, do not recursive call
                                        denominator = f[k]
                                        counterThree += 1
                                        # break
                                        break




# CODE FOR FINAL WHILE LOOP

                                        l = k
                                        # While loop
                                        while l < len(f):
                                            # If whitespace, skip
                                            if (f[l] == ' '):
                                                l += 1
                                                counterFour += 1
                                            # Else if there is '('
                                            elif (f[l] == '('):
                                                amountOfParenthesesTwo += 1
                                            # Else if there is ')'
                                            elif (f[l] == ')'):
                                                # If, must check amountOfParenthesesTwo to be equal to 0
                                                if (amountOfParenthesesTwo > 0):
                                                    l += 1
                                                    counterFour += 1
                                                    # Continue to find next ')'
                                                    continue
                                                # Else
                                                else:
                                                    # Denominator is from starting parentheses to current
                                                    denominator = f[k:l]
                                                    # break
                                                    break
                                            # Else there is normal numbers or symbols
                                            else:
                                                l += 1
                                                counterFour += 1
                                                continue