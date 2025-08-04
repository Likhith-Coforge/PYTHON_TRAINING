nums = (1,2,3,4,5)

result = list(map(lambda x: x**2 if x%2==0 else x**3,nums))

print(result)

nums = (1,2,3,4,5,6,7,8,9,101)

result_1 = list(filter(lambda x: x%2==0,nums))

print(result_1)

nums = (1,2,3,4,5,2,3,4,5,2,3)

from functools import reduce

result_2 = reduce(lambda x,y: x*y,set(nums))

print(result_2)