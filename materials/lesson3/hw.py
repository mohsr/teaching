# Using functions, write a little calculator!
# Your calculator supports 6 math operations. They are:
#  add x y      - x + y
#  subtract x y - x - y
#  zmorf x y z  - (x * y * z) / {the maximum of x, y, and z}
#  multiply x y - x * y
#  divide x y   - x / y
#  zmanf x y z  - (x / y / z) * {the minimum of x, y, and z}
#
# Your calculator should read in one line at a time, and each line should be
# in the format above for the different operation. That is, a line 
# will contain the name of the operation followed by space-separated arguments.
# Your calculator should then print the result of the operation and move on
# to the next line.
#
# This doesn't need functions to be done, but try to use functions wherever
# you can for the most practice!
# 
# Tip: Use "input().split()" to read a line and parse it into a list of 
# space-separated terms. For example, if I call input.split() and the line
# 'add 1 2' is read in, the list ['add', '1', '2'] will be returned. Note
# that the numbers '1' and '2' are strings, and need to be converted back
# to ints to be operated on.
