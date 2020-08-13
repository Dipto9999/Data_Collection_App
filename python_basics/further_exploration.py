##################
#### BOOLEANS ####
##################

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

#######################
###### FUNCTIONS ######
#######################

def addition_function(parameter_a,parameter_b) :
    result = parameter_a + parameter_b
    print("Sum of " + str(parameter_a) + " and " + str(parameter_b) + " : " + str(result)) 
    return result

# Test if subtrction function working as intended.
print()
print ("******CHECK ADDITION FUNCTION******")
print()

addition_function(1,2)

def subtract_function(parameter_a,parameter_b) :
    result = parameter_a - parameter_b
    print("Difference of " + str(parameter_a) + " and " + str(parameter_b) + " : " + str(result)) 
    return result

# Test if subtrction function working as intended.
print()
print ("******CHECK SUBTRACTION FUNCTION******")
print()

subtract_function(1,2)

def combination_function(parameter_a,parameter_b) :
    print ("Perform Combination Calculation of " + str(parameter_a) + " and " + str(parameter_b))

    print("First Addition -> ", end = " ")
    sum_a = addition_function(parameter_a,parameter_b)

    print("Subtraction -> ", end = " ")
    difference_a = subtract_function(parameter_a,parameter_b)
    
    sum_b = sum_a + difference_a
    print ("Final Sum : " + str(sum_b))
    return sum_b

# Test if combination function working as intended.
print()
print ("****** CHECK COMBINATION FUNCTION ******")
print()

combination_function(1,2)

# Pay attention to this investment function.
# Relevant to app developed in workshop.
def investment(principal_amount, interest_rate, year) :
    total_profit = principal_amount * (1 + interest_rate) ** year
    net_profit = total_profit - principal_amount

    if interest_rate <= 0.5 :
        statement = "Less Interest"
    elif (interest_rate <= 1 ) :
        statement = "More Interest"
    elif interest_rate > 1 :
        statement = "Be Cautious! This is a Ponzi Scheme."

    return { 
        "Total Profit" : total_profit, 
        "Net Profit" : net_profit, 
        "Investment Evaluation" : statement
    }
    
# Test if the investment function working as intended.
print()
print ("****** CHECK INVESTMENT FUNCTION ******")
print()

print("Investment Outcome of Principal Amount 1000 and Interest Rate 0.5 over 2 Years (Should be Less Interest) : ", investment(1000, 0.5, 2))
print("Investment Outcome of Principal Amount 1000 and Interest Rate 0.9 over 2 Years (Should be More Interest) : ", investment(1000, 0.9, 2))
print("Investment Outcome of Principal Amount 1000 and Interest Rate 1.5 over 2 Years (Should be Ponzi Scheme) : ", investment(1000, 1.5, 2))

