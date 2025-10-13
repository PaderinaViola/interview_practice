# Given an array of integers nums, calculate and return the sum of all the positive numbers. Numbers that are negative or zero should be ignored and skipped during the summation using continue.
nums = [-1, -5, -10]
total = 0
for i in nums:
    if i > 0:
        total += i
    else:
        continue
print(total) 