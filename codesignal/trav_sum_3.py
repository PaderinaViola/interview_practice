#Given a non-negative integer n, return a new integer where every digit of n is duplicated.
n = 0
def f(n):
    arr = []
    #first we need to add all of that to array, then multiply it and sort, convert to string and back then
    if n == 0:
        return 0
    while n > 0:
        n_new = n % 10
        n = n // 10
        arr.append(n_new)
    arr = arr *2
    arr.sort()
    numb = 0
    numb = int("".join(str(i) for i in arr))
    return(numb)
print(f(n))

