# Given an integer x, return true if x is a palindrome, and false otherwise. An integer is a palindrome when it reads the same backward as forward.
# Note: You must solve this without converting the integer to a string.

x = 121
def palindrome(x:int):
    array_orig = []
    array_2 = []
    while x > 0:
        numb = x % 10
        array_2.append(numb) 
        x = x // 10
    left = 0
    right = len(array_2) - 1
    while left < right:
        if array_2[left] == array_2[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

print(palindrome(x))

