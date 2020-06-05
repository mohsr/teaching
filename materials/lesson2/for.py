x = range(int(input("What's a positive integer?"))) # range(x) returns a list of all numbers from 0...x-1 *

sum = 0
for num in x: # Num is the current element in x
	sum += num

print("The sum is %s" % str(sum))




# * NOTE: range doesn't actually return a list (I think), but we can pretty much pretend that it does
