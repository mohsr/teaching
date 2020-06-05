
x = 1 
# Because x is not created inside a nested block of code, it has global scope,
# meaning it can be used anywhere
if True:
	y = 0
	# Because y is created inside this if-statement, it can only be used
	# inside this if statement

	print(x)

y = "hello"
# Because the previous variable y is not accessible in the current scope, this
# variable is, in fact, an entirely new variable

# If, elif, if-else, for loops, while loops, and function bodies all have their
# own scopes. If there is an indented block of code, that can be treated as its
# own scope.
