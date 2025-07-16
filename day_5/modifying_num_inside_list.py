nums = [123, 678, 9001]
print(nums)
nums[2] = list(str(nums[2]))
nums[2][2]='2'
nums[2]="".join(nums[2])
nums[2]=int(nums[2])
print(nums)