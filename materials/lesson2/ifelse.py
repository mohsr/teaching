# The if-block will always run here, but the else-block will never run
if True:
	print("Hi!")
else:
	print("This will never run")

x = int(input("Hi! What's an even number?\n"))
if x % 2 == 0:
	print("That is even, good math!")
else:
	print("That's not even :(")
