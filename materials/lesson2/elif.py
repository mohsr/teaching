x = input("Hi, what's a word that start with a lowercase 'h', 'f', 'r', or 'b'?\n")
# Initialize firstchar to the first letter in the input
firstchar = x[0]

# Depending on the first character of the input, one of the below blocks will be executed
# Please note that these blocks can contain more than just one line!
if (lower(firstchar) == "h"):
	print("That starts with an 'h'!")
elif (firstchar == "f"):
	print("That starts with an 'f'!")
elif (firstchar == "r"):
	print("That starts with an 'r'!")
elif (firstchar == "b"):
	print("That starts with a 'b'!")
else:
	print("That doesn't start with an 'h', 'f', 'r', or 'b' :(")
