#You are given an array of integers nums and two integers lower and upper. Return the count of elements in nums that are greater than or equal to lower and less than or equal to upper.
nums = [10, 20, 30]
def problem(nums, lower, upper):
    count = 0
    for num in nums:
        if num >= lower and num <= upper:
            count += 1
    return count

print(problem(nums, 1, 9))
print(eval('3+8'))