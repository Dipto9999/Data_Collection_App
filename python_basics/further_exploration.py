##################
###BOOLEANS#######
integer_g = 2
integer_h = 3

boolean_a = integer_g == integer_h
print("Are Equal? :", boolean_a)

boolean_b = integer_g != integer_h
print("Aren't Equal? :", boolean_b)

boolean_c = integer_g > integer_h
print(str(integer_g) + " > " + str(integer_h) + " ? :", boolean_c)

print("Is " + str(integer_g) + " Less Than " + str(integer_h) + "? :", (integer_g < integer_h)) 
print("Is " + str(integer_g) + " Greater Than or Equal To " + str(integer_h) + "? :", (integer_g >= integer_h))
print("Is " + str(integer_g) + " Less Than or Equal To " + str(integer_h) + "? :", integer_g <= integer_h)

##################
###FUNCTIONS######
def addition_function(parameter_a,parameter_b) :
    result = parameter_a + parameter_b
    return result
print("Sum of 1 & 2:", addition_function(1,2))

def subtract_function(parameter_a,parameter_b) :
    result = parameter_a - parameter_b
    return result
print("Difference of 1 & 2:", subtract_function(1,2))

def combination_function(parameter_a,parameter_b) :
    sum_a = addition_function(parameter_a,parameter_b)
    print("First Addition:", sum_a)
    difference_a = subtract_function(parameter_a,parameter_b)
    print("Subtraction:", difference_a)
    sum_b = sum_a + difference_a
    return sum_b
print("Final Sum:", combination_function(1,2))

# Pay attention to this investment function.
# Relevant to app developed in workshop.

```python
def investment(principal, interest, year) :
    total_profit = principal * (1 + interest) ** year
    net_profit = total_profit - principal

    if interest <= 0.5 :
        statement = "Less Interest"
    elif (interest <= 1 ) :
        statement = "More Interest"
    elif interest > 1 :
        statement = "Be Cautious! This is a Ponzi Scheme."

    return total_profit, net_profit, statement
```

# Test if investment function working as intended.
print("Investment Outcome (Should be Less Interest):", investment(1000, 0.5, 2))
print("Investment Outcome (Should be More Interest):", investment(1000, 0.9, 2))
print("Investment Outcome (Should be Ponzi Scheme):", investment(1000, 1.5, 2))

