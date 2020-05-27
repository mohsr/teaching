# The next line initializes my_name as a variable and gives it a value
my_name = input("What is your name?\n")
print("Hello %s!" % my_name)

# This is a function! Don't worry too much about how it's defined for now
def addition(num1, num2):
	return num1 + num2

# This is a comment!
print("Let's do some addition!\n")
num1     = input("What is the first number?\n")
num2     = input("What is the second number?\n")
sum_nums = addition(int(num1), int(num2))
print("The sum of %s and %s is: %s\n" % (num1, num2, str(sum_nums)))

