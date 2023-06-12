# Stephen Brown
# Taylor Series / Mclaurin Series Expansion

<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc">
	<ul class="toc-item">
		<li><span><a href="#Defined-Functions" data-toc-modified-id="Defined-Functions-1"><span class="toc-item-num">1.&nbsp;&nbsp;</span>Defined Functions</a></span>
			<ul class="toc-item">
				<li><span><a href="#Function-to-Display" data-toc-modified-id="Function-to-Display-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Function to Display</a></span></li>
				<li><span><a href="#Function-to-Display-Helper" data-toc-modified-id='Function-to-Display-Helper-1.2'><span class='toc-item-num'>1.2&nbsp;&nbsp;</span>Function to Display Helper</a></span></li>
				<li><span><a href="#Find-Complete-Parentheses" data-toc-modified-id='Find-Complete-Parentheses-1.3'><span class='toc-item-num'>1.3&nbsp;&nbsp;</span>Find Complete Parentheses</a></span></li>
				<li><span><a href="#Derivatives-for-Taylor-Expansion" data-toc-modified-id="Derivatives-for-Taylor-Expansion-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Derivatives for Taylor Expansion</a></span></li>
				<li><span><a href="#Display-Taylor-Expansion" data-toc-modified-id="Display-Taylor-Expansion-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Display Taylor Expansion</a></span></li>
				<li><span><a href="#Taylor-Expansion-Terms" data-toc-modified-id="Taylor-Expansion-Terms-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Taylor Expansion Terms</a></span></li>
				<li><span><a href="#Display-Taylor-Expansion-Terms" data-toc-modified-id="Display-Taylor-Expansion-Terms-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Display Taylor Expansion Terms</a></span></li>
				<li><span><a href="#Taylor-Expansion-Sums" data-toc-modified-id="Taylor-Expansion-Sums-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Taylor Expansion Sums</a></span></li>
				<li><span><a href="#Display-Taylor-Expansion-Sums" data-toc-modified-id="Display-Taylor-Expansion-Sums-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Display Taylor Expansion Sums</a></span></li>
				<li><span><a href="#Convergence" data-toc-modified-id="Convergence-1.10"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Convergence</a></span></li>
				<li><span><a href="#Percent-Error" data-toc-modified-id="Percent-Error-1.11"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>Percent Error</a></span></li>
			</ul>
		</li>
		<li><span><a href="#Main-Method" data-toc-modified-id="Main-Method-1"><span class="toc-item-num">2.&nbsp;&nbsp;</span>Building a Multiple Linear Regression Model</a></span>
			<ul class="toc-item">
				<li><span><a href="#User-Input" data-toc-modified-id="User-Input-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>User Input</a></span></li>
				<li><span><a href="#Power-Series" data-toc-modified-id="Power-Series-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Power Series</a></span></li>
				<li><span><a href="#Convergence-and-Divergence" data-toc-modified-id="Convergence-and-Divergence-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Convergence and Divergence</a></span></li>
				<li><span><a href="#Evaluated-Percent-Error" data-toc-modified-id="Evaluated-Percent-Error-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Evaluated Percent Error</a></span></li>
			</ul>
		</li>
	</ul>
</div>

# FMU Class Problem Arose In
**Math 203** - Calculus III, taught by Dr. Damon Scott.

# What Makes Problem Interesting
From the moment I was taught what a Taylor Series was, I immediately noticed just how much easier it would be if I could somehow program the computer to do it for me.

The first thing we did to actually compute values for the Taylor Series and Mclaurin Series was by going into Excel and plotting a large amount of different variables that change. This led me to my reasons.
* Reasons I thought a program would be easier:
    * For each iteration, you needed to find the next derivative
    * The iterations are going to infinity
    * Having to manually check to see how the series acted with each iteration
    * Having to manually input everything into Excel to make the Taylor Series

All of these issues have been fixed and simplified in this program.

# Method for Solving It
* Defined Function List:
    * Function for interpreting user inputted function
        * Converting string into a format that Math and Latex can understand and display
    * Function to help the previous function
        * This function is exactly the same as the previous function, besides that it does not display anything, and allows for recursion
    * Function to find the full set of numbers between parentheses
        * This function will find the ending of a parentheses
    * Function to find the first specified amount of derivatives of the function at point `a`
        * Using sympy, creates a list of the specified amount of derivatives evaluated at point `a`
    * Function to display the Taylor Series (or Mclaurin Series)
        * This function just takes the derivative list and displays the proper Taylor Series (or Mclaurin Series)
    * Function to find the actual values of the Taylor Series (or Mclaurin Series)
        * This function finds the actual values of each term in the Taylor Series (or Mclaurin Series)
    * Function to display the terms of the Taylor Series (or Mclaurin Series)
        * This function displays the evaluated terms of the Taylor Series (or Mclaurin Series)
    * Function to find the partial sums of the Taylor Series (or Mclaurin Series)
        * This function finds the partial sums of the Taylor Series (or Mclaurin Series) at the point `x`
    * Function to display the partial sums of the series
        * Using Latex and Math, the partial sums of the Taylor Series (or Mclaurin Series) are displayed
    * Function to find if the Taylor Series (or Mclaurin Series) converges
        * Figures out if the Taylor Series (or Mclaurin Series) converges by comparing the last two terms
        * If the round function sees that the two of them are the same number, then the Taylor Series (or Mclaurin Series) converges
        * If the numbers are different, then it will return that it diverges
        * This function will return boolean values and a string value
        * True for convergence
        * 'maybe' for if it is seen to be converging
        * False for divergence
    * Function to find the percent error between actual value and Taylor Series (or Mclaurin Series) value
        * Calculates the percent error between the final partial sum of the Taylor Series and the actual function value
        * This only occurs if the series converges


* Main Method
    * Ask user for a function that they want to make a Taylor Series (or Mclaurin Series) out of
    * Ask user for what point the Taylor Series should use to be centered around
    * Ask user for how many iterations should be done
    * Function call to derivative function
    * Display the first five terms of the Taylor Series using the derivatives list
    * Ask user for an x-value
    * Call is made to the function that finds the actual terms of the Taylor Series (or Mclaurin Series)
    * List of terms is created
    * Call is made to the function that finds the partial sums of the Taylor Series (or Mclaurin Series)
    * List of partial sums is created
    * Call to function to see if Taylor Series (or Mclaurin Series) converges or diverges
    * If Taylor Series (or Mclaurin Series) converges, calls percent error function for calculation
    * If Taylor Series (or Mclaurin Series) possibly converges, still calls percent error function and prints out warning
    * Else if series diverges, states that percent error cannot be found

## Taylor Series and Mclaurin Series:
* Every function can be approximated by a Taylor Series Expansion
* Using the power of Taylor Series Expansion, we can create an estimated function for functions such as sin(x), cos(x), e^x, and many others
* Taylor Series are based around a point, which we just state is `a`
* If `a` is 0, then the Taylor Series is called a Mclaurin Series


```python
from IPython.display import display, Math, Latex
import sympy as sp
import numpy as np
import math
```

* **Taylor Series Formula:**


```python
display(Math(r'$T(x)=\sum_{n=0}^\infty \frac{f^n(a)}{n!} \cdot (x-a)^n$'))
```


$\displaystyle T(x)=\sum_{n=0}^\infty \frac{f^n(a)}{n!} \cdot (x-a)^n$


* **Mclaurin Series Formula:**


```python
display(Math(r'$M(x)=\sum_{n=0}^\infty \frac{f^n(0)}{n!} \cdot x^n$'))
```


$\displaystyle M(x)=\sum_{n=0}^\infty \frac{f^n(0)}{n!} \cdot x^n$


# Defined Functions

## The following are all the functions that I defined to make the program work

### Function to Display

* Purpose of function: Accepts in user-inputted mathematical Python expression representing a function and converts it into an expression for Latex to display
* How it works:
    * Creates an empty list to store strings
    * While loop traverses user-inputted string (mathematical Python expression)
    * Function converts multiplication symbol to Latex expression
    * Function converts exponent symbol to Latex expression
    * Function converts fraction symbol to Latex expression
    * Function converts parentheses to Latex expression
    * The join function is then used on the list of strings to form the final string to display
    * Math and Latex display function is then used, which accepts in a raw string
    * Using the format function, the string list is added into the raw string
        * Format function used in a string 
        * {} is placed in the string, and the format function accepts the other string as a parameter
        * {} is replaced by the string entered as a parameter of the format function
    * The display function then displays the proper function


```python
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
        # If symbol is just whitespace
        elif (f[char] == ' '):
            char += 1
            continue
        # If symbol is a parentheses
        elif (f[char] == '('): 
            counter = 1
            i = char + 1
            partial_function = f[i:(len(f))]
            parentheses_function_return = find_complete_parentheses(partial_function)
            counter = counter + parentheses_function_return[0][0]
            first_parentheses = parentheses_function_return[0][1]
            char += counter
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
                    str_list.append(r'{')
                    str_list.append(final_first_parentheses)
                    str_list.append('')
            # There is no more characters, so just place act as if there is no fraction
            else:
                final_first_parentheses = function_to_display_helper(first_parentheses)
                str_list.append(r'{')
                str_list.append(final_first_parentheses)
                str_list.append('}')
                char += 1
            continue

        # If symbol is an ending parentheses
        elif (f[char] == ')'):
            str_list.append('}')

        # If next symbol is division, make a fraction
        elif(f[char] == '/'):
            del(str_list[len(str_list) - 1])
            if (f[char + 1] == '('):
                counter = 2
                i = char + 2
                partial_function = f[i:(len(f))]
                parentheses_function_return = find_complete_parentheses(partial_function)
                counter = counter + parentheses_function_return[0][0]
                full_parentheses = parentheses_function_return[0][1]
                denominator = function_to_display_helper(full_parentheses)
                str_list.append(r' \frac{')
                str_list.append(f[char - 1])
                str_list.append(r'}{')
                str_list.append(denominator)
                char += counter
            else:
                str_list.append(r' \frac{')
                str_list.append(f[char - 1])
                str_list.append(r'}{')
                str_list.append(f[char + 1])
                str_list.append(r'}')
                char += 2
            continue
        
        # Else it is just a number, +, or -
        else:
            str_list.append(f[char])
        char += 1
        
    function = ''.join(str_list)
    # The function I use here is used many times throughout my program. This is a Latex function,
    # which also uses the Math package, and will print out the mathematical values and expressions
    # in a more impressive fashion, rather than printing them out normally.
    display(Math(r'$f(x)={}$'.format(function)))
```

### Function to Display Helper

* Purpose of function: Accepts in a sliced string to evaluate the numbers that are in the set of parentheses. This function allows for recursion, that why parentheses in parentheses can be evaluated.
* How it works:
    * Functions exactly the same as function_to_display
    * Only difference is that it is not displaying at the end, the function just joins the list of strings and returns the string to function_to_display


```python
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

        elif (f[char] == '('): 
            counter = 1
            i = char + 1
            partial_function = f[i:(len(f))]
            parentheses_function_return = find_complete_parentheses(partial_function)
            counter = counter + parentheses_function_return[0][0]
            first_parentheses = parentheses_function_return[0][1]
            char += counter
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
                    str_list.append(r'{')
                    str_list.append(final_first_parentheses)
                    str_list.append('')
            # There is no more characters, so just place act as if there is no fraction
            else:
                final_first_parentheses = function_to_display_helper(first_parentheses)
                str_list.append(r'{')
                str_list.append(final_first_parentheses)
                str_list.append('}')
                char += 1
            continue

        # If symbol is an ending parentheses
        elif (f[char] == ')'):
            str_list.append('}')

        # If next symbol is division, make a fraction
        elif(f[char] == '/'):
            del(str_list[len(str_list) - 1])
            if (f[char + 1] == '('):
                counter = 2
                i = char + 2
                partial_function = f[i:(len(f))]
                parentheses_function_return = find_complete_parentheses(partial_function)
                counter = counter + parentheses_function_return[0][0]
                full_parentheses = parentheses_function_return[0][1]
                denominator = function_to_display_helper(full_parentheses)
                str_list.append(r' \frac{')
                str_list.append(f[char - 1])
                str_list.append(r'}{')
                str_list.append(denominator)
                char += counter
            else:
                str_list.append(r' \frac{')
                str_list.append(f[char - 1])
                str_list.append(r'}{')
                str_list.append(f[char + 1])
                str_list.append(r'}')
                char += 2
            continue
        
        # Else it is just a number, +, or -
        else:
            str_list.append(f[char])
        char += 1
        
    function = ''.join(str_list)
    return function
```

### Find Complete Parentheses

* Purpose of function: Accepts in a sliced function and will return a list of a tuples where the first piece of data is how many characters were traversed, and second is the complete parentheses
* How it works:
    * Creates an empty list to store strings
    * Creates a counter
    * Initializes first_parentheses variable
    * Executes a while loop to traverse the sliced string with a set of conditional statements
        * If there is blank space, the code skips it
        * If there is another starting parentheses, the more_parentheses variable increments, meaning that another ')' must be found
        * If ')' is found, it checks to make sure that there is no need to search for another ')'
        * If that is the last parentheses, it slices the string and stores it in the first_parentheses variable
        * The tuple of the counter and the first_parentheses are returned


```python
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
```

### Derivatives for Taylor Expansion

* Purpose of function: Accepts in the user-inputted mathematical Python expression, the a-value, and the amount of iterations for this Taylor Series or Mclaurin Series and will return a list of tuples, consisting of the derivative function and value
* How it works:
    * Creates an empty list to store derivatives
    * Uses while loop, where i just has to be less than or equal to the amount of iterations desired
    * When i is 0, the sympified version of the original function and the original function evaluated at `a` should be stored as a tuple in the list
    * When i is anything else, the previous function is taken from the list, and using sympy's diff() method, the higher derivative is found, and then stored in the tuple with the higher derivative being evaluated
    * Each time i increments, it is another derivative being taken until the iteration goal is met
    * After loop ends, list is returned


```python
def derivatives_for_taylor_expansion(f, a, n):
    list_of_derivatives = []
    i = 0
    while i <= n:
        if i == 0:
            # The function I use here is sympy's sympify method, which converts the string (which is a Python expression)
            # into a sympy expression. This provides me with a sympy expression that I can use to find the derivative.
            original_expression = sp.sympify(f)
            x = a
            original_value = eval(f)
            list_of_derivatives.append((original_expression, original_value))
        else:
            previous_expression = list_of_derivatives[i - 1][0]
            # The function I use here is sympy's diff method, which finds the derivative of a sympy expression.
            derivative_expression = previous_expression.diff()
            string_derivative_expression = str(derivative_expression)
            x = a
            derivative_value = eval(string_derivative_expression)
            list_of_derivatives.append((derivative_expression, derivative_value))
        i += 1
        
    return list_of_derivatives
```

### Display Taylor Expansion

* Purpose of function: Accepts the original user-inputted mathematical Python expression, the list of derivatives for it, and the a-value and will display the Taylor Series or Mclaurin Series in unsimplified terms
* How it works:
    * Creates an empty list for strings
    * Function will only display first five terms
    * While loop for while i is less than or equal to 5
    * Conditional statement with `a` to see if it is zero or not, determining if it is a Taylor Series or Mclaurin Series
    * Takes the derivatives from the original, then forms and displays the unsimplified Taylor Series or Mclaurin Series terms


```python
def display_taylor_expansion(f, df_list, a):
    str_list = []
    i = 0
    while i <= 5:
        if (i == 0):
            str_list.append(str(df_list[i][1]))
            str_list.append(r'+')
        elif (i == 1):
            str_list.append(r'{(')
            str_list.append(str(df_list[i][1]))
            str_list.append(r' \cdot x)}+')
        else:
            str_list.append(r'{( \frac{')
            str_list.append(str(df_list[i][1]))
            str_list.append(r'}{')
            str_list.append(str(i))
            str_list.append(r'!} \cdot x^{')
            str_list.append(str(i))
            str_list.append(r'})}+')
        i += 1
    str_list.append(r' \ldots')
    if (a == 0):
        mclaurin_series = ''.join(str_list)
        print('The Mclaurin Series expansion for')
        function_to_display(f)
        print('is')
        display(Math(r'$M(x)={}$'.format(mclaurin_series)))
    else:
        taylor_series = ''.join(str_list)
        print('The Taylor Series expansion for')
        function_to_display(f)
        print('is')
        display(Math(r'$T(x)={}$'.format(taylor_series)))
```

### Taylor Expansion Terms

* Purpose of function: Takes in the user-inputted x-value for the Taylor Series or Mclaurin Series along with the amount of iterations and the list of derivatives, and then returns a list of floats consisting of the simplified terms in the series
* How it works:
    * Creates an empty list for floats
    * While loop for iterations
    * If it is the first iteration, only append the first value of the derivatives list to the new list
    * Else if it is the second iteration, only append the second value of the derivatives list multiplied by (x - a)
    * Else append the derivative divided by the factorial of the iteration number, and then multiplied by (x - a) raised to the power of the iteration number
    * Returns the list of terms of the series


```python
def taylor_expansion_terms(x, a, n, list_derivatives):
    list_of_taylor_terms = []
    i = 0
    while i <= n:
        if (i == 0):
            list_of_taylor_terms.append(list_derivatives[i][1])
        elif (i == 1):
            term = list_derivatives[i][1] * (x - a)
            list_of_taylor_terms.append(term)
        else:
            # The function I use here is the math package's factorial method. Originally, I had predefined my own
            # factorial method, but the numbers became so large so quickly that it was causing the program to overflow.
            # This method simply finds the factorial and returns it.
            denominator = math.factorial(i)
            fraction = list_derivatives[i][1] / denominator
            x_value = (x - a)**i
            term = fraction * x_value       
            list_of_taylor_terms.append(term)
        i += 1
            
    return list_of_taylor_terms
```

### Display Taylor Expansion Terms

* Purpose of function: Takes in the list of Taylor Expansion terms along with the user-inputted a-value and displays the Taylor Series or Mclaurin Series with the evaluated terms.
* How it works:
    * Creates an empty list for strings
    * While loop for the first five terms
    * Appends the terms to the list
    * Conditional statement to figure out whether `a == 0`, which determines if it displays a Mclaurin Series or a Taylor Series
    * Joins the list of strings into a string and then uses the format function to place the string into the raw string within the Latex and Math display function


```python
def display_taylor_expansion_terms(list_terms, a):
    str_list = []
    i = 0
    while i <= 5:
        str_list.append(str(list_terms[i]))
        str_list.append(r'+')
        i += 1
    str_list.append(r' \ldots')
    if (a == 0):
        mclaurin_series = ''.join(str_list)
        print('\nThe terms for the Mclaurin Series expansion:')
        display(Math(r'$M(x)={}$'.format(mclaurin_series)))
    else:
        taylor_series = ''.join(str_list)
        print('\nThe terms for the Taylor Series expansion:')
        display(Math(r'$T(x)={}$'.format(taylor_series)))
```

### Taylor Expansion Sums

* Purpose of function: Takes in the list of the terms in the Taylor Series or Mclaurin Series and returns a list containing each of the partial sums, according to how many iterations were done on them.
* How it works:
    * Creates an empty list for floats
    * Initialize partial_sum variable to be 0
    * For loop that goes through each term
    * With each term, or each iteration, the term is added to the partial_sum variable
    * The partial_sum is then appended to the list
    * The list of partial sums is then returned


```python
def taylor_expansion_sums(list_terms):
    list_of_sums = []
    partial_sum = 0.0
    for term in list_terms:
        partial_sum = partial_sum + term
        list_of_sums.append(partial_sum)
    return list_of_sums
```

### Display Taylor Expansion Sums

* Purpose of function: Takes in the list of partial sums, the user-inputted a-value, and the user-inputted number of iterations and will display each of the Taylor Series or Mclaurin Series partial sums.
* How it works:
    * Conditional statement to make sure that the number of iterations is greater than 8
    * If the number of iterations is greater than 8, then check to see if the series is a Taylor Series or Mclaurin Series by a == 0
        * Two while loops
        * First while loop will create an empty string list
        * The while loop will then append all the pieces of the string needed to print the partial sum
        * Using the list, it will join the strings and place it in the raw string in the display function using the format function
        * The second while loop will do the same, but the difference is that it will do it with the last three terms by setting i equal to the number of iterations minus 2
    * Else the iterations is less than 8, which means that all of the Taylor Series or Mclaurin Series partial sums should be printed out.
        * One while loop and a conditional statement to see if series is Taylor Series or Mclaurin Series
        * The same process is used from before


```python
def display_taylor_expansion_sums(list_sums, a, n):
    # If n is more than 8
    if (n > 8):
        if (a == 0):
            print('\nThe partial sums for the Mclaurin Series are:')
        else:
            print('\nThe partial sums for the Taylor Series are:')
        i = 0
        while i <= 5:
            str_list = []
            if (a == 0):
                str_list.append(r'M_')
            else:
                str_list.append(r'T_')
            str_list.append(str(i))
            str_list.append(r'(x)=')
            str_list.append(str(list_sums[i]))
            if (a == 0):
                mclaurin_series = ''.join(str_list)
                display(Math(r'${}$'.format(mclaurin_series)))
            else:
                taylor_series = ''.join(str_list)
                display(Math(r'${}$'.format(taylor_series)))
            i += 1
        # Display ...
        display(Math(r' \ldots'))
        # Display last three terms
        i = round(n - 2)
        while i <= n:
            str_list = []
            if (a == 0):
                str_list.append(r'M_{')
            else:
                str_list.append(r'T_{')
            str_list.append(str(i))
            str_list.append(r'}(x)=')
            str_list.append(str(list_sums[i]))
            if (a == 0):
                mclaurin_series = ''.join(str_list)
                display(Math(r'${}$'.format(mclaurin_series)))
            else:
                taylor_series = ''.join(str_list)
                display(Math(r'${}$'.format(taylor_series)))
            i += 1
    # If n is less than or equal to 8
    else:
        i = 0
        while i <= n:
            str_list = []
            if (a == 0):
                str_list.append(r'T_')
            else:
                str_list.append(r'M_')
            str_list.append(str(i))
            str_list.append(r'(x)=')
            str_list.append(str(list_sums[i]))
            if (a == 0):
                mclaurin_series = ''.join(str_list)
                display(Math(r'${}$'.format(mclaurin_series)))
            else:
                taylor_series = ''.join(str_list)
                display(Math(r'${}$'.format(taylor_series)))
            i += 1
```

### Convergence

* Purpose of function: Takes in the list of partial sums of the Taylor Series or Mclaurin Series and will return true if the series converges, false if the series diverges, or 'maybe' if the series seems to be converging.
* How it works:
    * The next to last partial sum is saved into a variable
    * The last partial sum is saved into a variable
    * Conditional statement is then used for the three cases
    * If the last partial sum, when rounded to 4 decimal places, is equal to the previous partial sum, when rounded to 4 decimal places, the series is seen to converge and returns True
    * If the absolute value of the difference between the last partial sum and the next to last partial sum is less than or equal to 0.1, then it returns 'maybe', considering that the series has not completely converged but shows signs that it might
    * Else the series does not converge at all, which means that it must diverge and returns False


```python
def convergence(partial_sums_list):
    next_to_last_partial_sum = partial_sums_list[len(partial_sums_list) - 2]
    last_partial_sum = partial_sums_list[len(partial_sums_list) - 1]
    # If the last and previous partial sums are exactly the same when rounded, converges
    if (round(next_to_last_partial_sum, 4) == round(last_partial_sum, 4)):
        return True
    
    # If the last and previous partial sums are off by .1, it "will probably converge"
    elif (abs(last_partial_sum - next_to_last_partial_sum) <= .1):
        return 'maybe'
    
    # Else it diverges
    else:
        return False
```

### Percent Error

* Purpose of function: Takes in the list of partial sums, the original user-inputted mathematical Python expression, and the x-value that the user inputted, and if the series is seen to converge or might converge, will compute the percent error of the approximation to the actual function. 
* How it works:
    * The final partial sum from the list is saved into a variable
    * x is set equal to user_x, so that the eval function will be able to compute the actual function's value
    * The actual value is then saved to a variable using the eval function on the original user-inputted function
    * The fraction for the percent error formula is evaluated and stored in a variable
    * The percent error is then found by the abs function finding the absolute value of the fraction and then multiplying by 100%
    * The percent error is then returned


```python
def percent_error(partial_sums_list, function, user_x):
    value_observed = partial_sums_list[len(partial_sums_list) - 1]
    x = user_x
    value_expected = eval(function)
    fraction = (value_observed - value_expected) / value_expected
    percent_error = abs(fraction) * 100
    return percent_error
```

# Main Method

### User Input

* Purpose: This portion of code works for the user inputting the first part of the necessary information: the function, the a-value, and the amount of iterations to be evaluated.
* How it works:
    * While True loop to ask the user to enter a mathematical Python expression representing a function
        * Input function is executed and stored in a variable
        * The function_to_display function is then called with the user's input as a parameter
        * The user is then asked if the function is correct
        * If the user enters 'y' or 'Y', then while True loop is broken
        * If the user enters 'n' or 'N', then the while True loop repeats
        * If the input is not recognized, the while True loop repeats
    * While True loop to ask the user to enter the a-value for the series expansion
        * Input function is executed and stored in a variable
        * The a-value is then placed inside of the Math and Latex display function and displayed
        * If the user enters 'y' or 'Y', then while True loop is broken
        * If the user enters 'n' or 'N', then the while True loop repeats
        * If the input is not recognized, the while True loop repeats
    * While True loop to ask the user how many iterations (terms) they want the series to go out to
        * Input function is executed and stored in a variable
        * If the input is less than or equal to 0, the code will state that it is not possible and then repeat the while True loop
        * If the input is less than or equal to 5, the code will state that the terms must be more than 5
        * Else the loop will be broken
    * derivatives_for_taylor_expansion is then called and stored in a variable
    * display_taylor_expansion is then called to display the Taylor Series or Mclaurin Series 


```python
# Ask user for a function that they want to make a Taylor Series (or Mclaurin Series) out of
while True:
    user_function = input('Enter a function in terms of x:\n')
    function_to_display(user_function)
    user_input = input('Is this correct? Y/N\n')
    if user_input == 'y' or user_input == 'Y':
        break
    elif user_input == 'n' or user_input == 'N':
        continue
    else:
        print('Input is not recognized. Try again.')
        continue
        
# Ask user for what point the Taylor Series should use
while True:
    user_a = float(input('Enter the value of a that you want the series to be based around:\n'))
    display(Math(r'$a={}$'.format(user_a)))
    user_input_two = input('Is this the correct a-value? Y/N\n')
    if user_input_two == 'Y' or user_input_two == 'y':
        break
    else:
        continue

# Ask how many terms the user wants it to go out to
while True:
    user_n = float(input('Enter the amount of iterations you would like the series to go to:\n'))
    if (user_n <= 0):
        print('You cannot have terms that are less than or equal to zero, and terms must be greater than five. Try again.')
        continue
    elif (user_n <= 5):
        print('Must have more than five iterations. Try again.')
    else:
        break

# Function call to derivative function
derivatives = derivatives_for_taylor_expansion(user_function, user_a, user_n)

# Display the first five terms of the Taylor Series using the derivatives list
display_taylor_expansion(user_function, derivatives, user_a)
```

    Enter a function in terms of x:
    1**x
    


$\displaystyle f(x)=1^x$


    Is this correct? Y/N
    y
    Enter the value of a that you want the series to be based around:
    0
    


$\displaystyle a=0.0$


    Is this the correct a-value? Y/N
    y
    Enter the amount of iterations you would like the series to go to:
    100
    The Mclaurin Series expansion for
    


$\displaystyle f(x)=1^x$


    is
    


$\displaystyle M(x)=1.0+{(0 \cdot x)}+{( \frac{0}{2!} \cdot x^{2})}+{( \frac{0}{3!} \cdot x^{3})}+{( \frac{0}{4!} \cdot x^{4})}+{( \frac{0}{5!} \cdot x^{5})}+ \ldots$


### Series Evaluation

* Purpose: This portion of code will ask for the last piece of user input, the x-value. It will then evaluate and simplify all the terms of the Taylor Series or Mclaurin Series, then it will print out the list of the partial sums of the series.
* How it works:
    * The user is asked to enter the value for x, and then the input is stored in a variable
    * The taylor_expansion_terms function is then called and the list of terms is stored in a variable
    * The display_taylor_expansion_terms function is called to display the evaluated and simplified terms of the Taylor Series or Mclaurin Series
    * The taylor_expansion_sums function is then called and the list of partial sums is stored in a variable
    * The display_taylor_expansion_sums function is called and prints out the list of partial sums


```python
# Ask user for an x-value
user_x = float(input('Enter the x-value that you would like to approximate:\n'))

# Display Taylor (Mclaurin) Series with the proper terms (other words: with x plugged in)
series_terms = taylor_expansion_terms(user_x, user_a, user_n, derivatives)
display_taylor_expansion_terms(series_terms, user_a)

# Call is made to the function that finds the actual values of Taylor Series and returns the list of the first 100 terms
series_partial_sums = taylor_expansion_sums(series_terms)

# Display Series of Partial Sums
display_taylor_expansion_sums(series_partial_sums, user_a, user_n)
```

    Enter the x-value that you would like to approximate:
    .5
    
    The terms for the Mclaurin Series expansion:
    


$\displaystyle M(x)=1.0+0.0+0.0+0.0+0.0+0.0+ \ldots$


    
    The partial sums for the Mclaurin Series are:
    


$\displaystyle M_0(x)=1.0$



$\displaystyle M_1(x)=1.0$



$\displaystyle M_2(x)=1.0$



$\displaystyle M_3(x)=1.0$



$\displaystyle M_4(x)=1.0$



$\displaystyle M_5(x)=1.0$



$\displaystyle  \ldots$



$\displaystyle M_{98}(x)=1.0$



$\displaystyle M_{99}(x)=1.0$



$\displaystyle M_{100}(x)=1.0$


### Radius / Interval of Convergence 

* Whenever a series converges, it has many different ways that it can converge
* It can converge absolutely, conditionally, or not at all
* The radius, or interval, between the x's where the series converges is called the radius of convergence
* The program does not find the radius of convergence, but if the radius of convergence for a series is known, it can be tested with this program to see the series converge

### Convergence and Divergence

* Purpose: This portion of code evaluates whether or not the series converges or not.
* How it works:
    * The convergence function is called with the list of partial sums as a parameter, which is then stored inside a variable
    * If the result of the series is True, then it will print that the series converges
    * If the result of the series is 'maybe', then it will print out the warning that the series appears to be converging, but it is not confirmed
    * Else the result of the series is false, then it will print out that it diverges


```python
result_of_series = convergence(series_partial_sums)
if (result_of_series == True):
    final_sum = series_partial_sums[len(series_partial_sums) - 1]
    print(f'The series converges to: {final_sum:.2f}')
elif (result_of_series == 'maybe'):
    print('At the maximum term selected, the series has shown signs of convergence, but the result is not confirmed. You might want to try again with a larger maximum term.')
    print(f'The series, to this iteration, converges to: {final_sum:.2f}')
else:
    print('The series diverges.')
```

    The series converges to: 1.00
    

### Evaluated Percent Error

* Purpose: This portion of code is meant to find the percent error between the series approximation and the actual value from the actual equation.
* How it works:
    * If the result of the series is that the series converges, then the percent_error function is called to determine the percent error and print it out.
    * If the percent error is 0, or rounds to 0, then it is seen as a perfect approximation
    * If the result of the series is that the series might converge, then the percent_error function is still called and printed out, but with the proper warnings
    * Else the series did not converge and the percent error cannot be evaluated

#### Percent Error Formula
* The percent error between an actual value and an observed value can be represented by the formula:


```python
display(Math(r'$P(x)=| \frac{observedValue - expectedValue}{expectedValue} | \cdot 100% $'))
```


$\displaystyle P(x)=| \frac{observedValue - expectedValue}{expectedValue} | \cdot 100% $



```python
if (result_of_series == True):
    error = round(percent_error(series_partial_sums, user_function, user_x), 2)
    if (error == 0.0):
        print('Perfect approximation! There is either no percent error or such a small percent error that it can be disregarded.')
    else:
        print('The percent error is: {}%'.format(str(error)))
elif (result_of_series == 'maybe'):
    error = round(percent_error(series_partial_sums, user_function, user_x), 2)
    if (error == 0.0):
        print('There is no percent error, but the convergence is not confirmed, so neither is the percent error.')
    else:
        print('The percent error is: {}%'.format(str(error)))
else:
    print('Percent error cannot be found because the series diverges')
```

    Perfect approximation! There is either no percent error or such a small percent error that it can be disregarded.
    
