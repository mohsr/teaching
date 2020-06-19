
# This is the definition of the function my_function
# name - my_function
# parameters - ints x, y, and z
#   Notice that while I say these are ints, and they are treated as
#   such by the function, Python does not do explicit type checking
#   to verify that the arguments given to the function are ints.
#   There is nothing to stop me from calling my_function(True, False, []).
#   If you like, Python gives a mechanism that lets you check the type
#   of a variable at runtime.
# return value - a string
#   Notice that in Python, the return value is not explicitly declared,
#   but rather it is whatever happens to be returned on a given call to
#   the function. A function can return an int sometimes or a string
#   sometimes (this inconsistency is probably bad practice). See
#   varying_ret_fun below for an example.
# The body of the function is everything indented within my_function.
# When I call my_function(1, 2, 3), the body runs with x = 1, y = 2, and z = 3.
#
# Note: my_function cannot be called before the function definition
#       has been parsed. Generally, this means calling my_function
#       will not work above the definition, but it will work after.
#       We can talk more about this, there's some nonobvious nuance.
def my_function(x, y, z):
	summed = x + y + z
	str_sum = "The sum is " + string(summed)
	return string(x + y + z)

# This function can return an int, a string, or a bool! Chaos!
def varying_ret_fun(string):
	if string == "int":
		return 42
	elif string == "string":
		return "a string"
	else:
		return True
