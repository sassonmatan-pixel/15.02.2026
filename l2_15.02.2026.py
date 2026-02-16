# nums = [7, 1, 9, 2, 2, 10]
# words = ["banana", "kiwi", "apple", "fig", "watermelon"]
'''
Do:
Print nums sorted ascending (without changing original)
Sort nums in-place descending
Print words alphabetically A→Z
Print words by length shortest→longest
Print words by length longest→shortest. hint: reverse=True
'''
from os import name

nums = [7, 1, 9, 2, 2, 10]
words = ["banana", "kiwi", "apple", "fig", "watermelon"]
new_nums = nums.copy()
nums.sort()
print(nums)
print(nums[::-1])
print(sorted(nums, reverse=True))
print(sorted(words))
print(sorted(words, key=len))
print(sorted(words, key=len, reverse=True))
