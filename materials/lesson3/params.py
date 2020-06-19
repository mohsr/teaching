# If primitive types are passed to this function, they are copied, and are
# thus passed by value.
def pass_by_value(x, y):
	# These modifications to x and y only exist inside this function
	x *= 2
	y *= 4
	# The return value is still calculated with the modified x and y
	return x + y

# If a list is passed to this function, a reference to it is given, so
# it is passed by reference.
# Also, note that this function doesn't return anything! Functions do
# not need to return any value.
def pass_by_reference(my_list):
	my_list.append("new list entry")

# This function can be called with either one argument or two. If only
# one is given, then y defaults to 10.
def default_fun(x, y=10):
	return x * y


# Pass-by-value demonstration
my_var = 1
pass_by_value(my_var, 12)
print(my_var)

# Pass-by-reference demonstration
my_list = []
pass_by_reference(my_list)
print(my_list)

# Default parameter demonstration
print(default_fun(7))
print(default_fun(7, 11))
