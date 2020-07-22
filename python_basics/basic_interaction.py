#############
###NUMERIC###
integer_a = 1
print("integer_a is assigned to 1:", integer_a)

integer_b = 3
print("integer_b is assigned to 3:", integer_b)

integer_c = integer_a + integer_b
print("Addition:", integer_c)

integer_d = integer_a - integer_b
print("Subtraction:", integer_d)

integer_e = integer_a * integer_b
print("Multiplication:", integer_e)

float_a = integer_a / integer_b
print("Division:", float_a)

integer_f = (integer_a + integer_b) * integer_b
print("BEDMAS: ", integer_f)

#############
###STRINGS###
string_a = "MUNTAKIM"
print("First Name:", string_a)

string_b = "RAHMAN"
print("Last Name:", string_b)

string_c = string_a + " " + string_b
print("Concatenation:", string_c)

string_d = "OLD"
# Note the use of str() function here to convert an integer to a string.
string_e = string_a + " " + string_b + " " + str(5) + " YEARS " + string_d
print("More Concatenation:", string_e)


