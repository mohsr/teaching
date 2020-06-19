# Filter has two parameters
#  predicate - a function that takes something from vals and returns a bool
#  vals - a list of values, each of which is a valid argument to predicate
def filter(predicate, vals):
	x = []
	for val in vals:
		if predicate(val):
			x.append(val)
	return x

def tautology(x):
	return True

def contradiction(x):
	return False

def is_even(x):
	return x % 2 == 0

my_list = range(9)
print(filter(tautology, my_list))
print(filter(contradiction, my_list))
print(filter(is_even, my_list))

# Bonus: You can even use 'lambda expressions' to dynamically create functions!
print(filter(lambda x: x % 2 != 0, my_list))
