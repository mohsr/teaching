# Normally, a "while True" loop runs forever
# Because of the break statement, it will only loop once
while True:
	print("Running an iteration...")
	break
	print("hi")
# For greater control, break statements can be nested inside if-statements
# inside the loop.

for x in range(10):
	if x % 2 == 0:
		continue # For all even numbers, we continue, so only odds will print
	print(x)

