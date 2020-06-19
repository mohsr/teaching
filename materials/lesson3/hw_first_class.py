####################### IGNORE THIS UNLESS UR CURIOUS #######################
import random
import string

# Generate a random peptide
def gen_peptide():
	peptide = (random.choice(string.ascii_letters) + 
	           random.choice(['', random.choice(string.ascii_letters)]) +
	           str(random.choice(range(10))) +
	           random.choice(['', random.choice(string.ascii_letters)]))
	return peptide.upper()

# Generate a random Kd, in nanomolar
def gen_kd():
	return random.randint(50, 2000)

# Generate a list of n peptide-Kd pairs
def gen_data(n):
	return [(gen_peptide(), gen_kd()) for i in range(n)]

############################# OK STOP IGNORING ##############################

# Extra credit! A Toofts University undergrad is hard at work processing
# data in the Applechild Chemistry building. Her data is a list of 
# peptide-kd pairs, but she only cares about the ones with a good kd value.
# Using the filter function defined below, write a function that takes a
# number and a list of peptide-kd pairs and removes all pairs with a kd
# less than the given number. When you're done, call your function and
# print the filtered list.
# 
# TIPS!
# The variable 'data' represents the data (the list of peptide-kd pairs). 
# To access the peptide name of a given pair p, write 'p[0]'.
# To access the kd of a given pair p, write 'p[1]'.
#
# Extra extra credit! Use a lambda function in your implementation. See
# first_class.py for an example of this.

def filter(predicate, vals):
	ret = []
	for val in vals:
		if (predicate(val)):
			ret.append(val)
	return ret

data = gen_data(500)
