def mean_of_nums(*args):
	""" Return the mean of any number of values"""
	return sum(args)/len(args)

print(mean_of_nums(1,2,3,4,5))