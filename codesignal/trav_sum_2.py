#Given a positive integer n, calculate and return the product of all of its even digits that are not zero.
#If the number has no non-zero even digits, return 1, as 1 is the identity for multiplication.
n = 246793
array = []
def f(n):
    while n > 0:
        new = n%10
        n = n//10
        if new % 2 == 0:
            array.append(new)
    product = 1
    for i in array:
        product *= i
    return product

print(f(n))

