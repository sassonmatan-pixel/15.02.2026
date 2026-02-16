'''
Exercise 1: The "Guest List" Cleaner
You have a list of names for a party, but some people signed up twice.
- Create a list called guests with these values: "Alice", "Bob", "Charlie", "Alice", "David", "Bob"
- Use a set to automatically remove the duplicates
- Check if "Emma" is in your set. If she is not there, add her
- Print the final number of unique guests using len()

Exercise 2: Safe Deletion Race
- Create a set called codes containing: 101, 102, 103, 104
- Use .pop() to remove one random code and print it
- Try to use .remove() to delete the number 999 --> ERROR!, so- Wrap it with if to avoid crash
- Use .discard() to delete the number 999
'''

# **BONUS**
# **BONUS**
# **BONUS**
# **BONUS**
# **BONUS**
import random
from multiprocessing.resource_sharer import stop

'''
random_nums = []

for i in range(30):
    num = random.randint(1, 10)
    random_nums.append(num)

print(random_nums)
'''
# print each number and how many times, without duplications
# hint: sort, set, count
# [1, 4, 2, 2, 1, 5]
# 1: 2-times
# 2: 2-times
# 4: 1-time
# 5: 1-time'''


'''
Exercise 1: The "Guest List" Cleaner
You have a list of names for a party, but some people signed up twice.
- Create a list called guests with these values: "Alice", "Bob", "Charlie", "Alice", "David", "Bob"
- Use a set to automatically remove the duplicates
- Check if "Emma" is in your set. If she is not there, add her
- Print the final number of unique guests using len()
'''
guests = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"]
guests = set(guests)
print(guests)
if not "Emma" in guests:
    guests.add("Emma")
print(guests)
print(f'the guest number is:{len(guests)}')

'''
Exercise 2: Safe Deletion Race
- Create a set called codes containing: 101, 102, 103, 104
- Use .pop() to remove one random code and print it
- Try to use .remove() to delete the number 999 --> ERROR!, so- Wrap it with if to avoid crash
- Use .discard() to delete the number 999
'''

codes = {"101", "102", "103", "104"}
codes.pop()
print(codes)
if 999 in codes:
    codes.remove(999)
    print(codes)
codes.discard(999)
print(f' no 999 here {codes}')


#********************************
random_nums = []
for i in range(10):
    num = random.randint(1, 10)
    random_nums.append(num)

set_random_nums = set(random_nums)
list_randon_nums = list(set_random_nums)
list_randon_nums.sort()
for num in list_randon_nums:
    print(f'{num}:is {random_nums.count(num)} times')
