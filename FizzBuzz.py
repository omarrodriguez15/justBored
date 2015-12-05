print 'My Fizz-Buzz program'
for num in range(101):
	output = str(num)
	if num % 3 == 0:
		output += ' Fizz'
	if num % 5 == 0:
		output += ' Buzz'
	print output