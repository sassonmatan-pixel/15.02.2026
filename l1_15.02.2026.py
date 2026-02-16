from itertools import count

nums = [5, 2, 1, 9, -4 ,2]
for num in nums:
    if nums.count(num) > 1:
        print("there is double number")
        break
else:
    print("there is no double number")

nums = [5, 2, 1, 9, -4 ,2]
while any(nums.count(num) > 1 for num in nums):
    print("there is double number")
    break
else:
    print("there is no double number")

nums = [5, 2, 1, 9, -4 ,2]
nums.sort()
for num in range(1, len(nums)):
    if nums[num] == nums[num - 1]:
        print("there is double number")
        break
else:
    print("there is no double number")

