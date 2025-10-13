# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
#eturn the indices of the two numbers (added by one) as an integer array [index1, index2] of length 2. You may assume that each input would have exactly one solution. You may not use the same element twice. Your solution must use only constant extra space.
numbers = [2, 7, 11, 15]
target = 9

def targ(numbers, target):
    i = 0
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return "didnt find shi"

print(targ(numbers, target))