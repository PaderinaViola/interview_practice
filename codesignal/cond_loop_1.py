#Given an array of integers nums, iterate through the array and return the first negative number you encounter. If no negative number exists in the array, return 0.
# Corrected Solution
nums = [2, 5, 8, -3, 4, 1]
found_negative = False
for i in nums:
    if i < 0:
        print(i)
        found_negative = True
        break

if not found_negative:
    print(0)
