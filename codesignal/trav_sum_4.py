# Given a non-negative integer n, return the count of groups of consecutive equal digits. A group consists of one or more identical digits next to each other.
n = 11222311
#again we will need to create an array from those numbers and then iterate through each, two pointers maybe??, the i should change after the diff number in j found
def f(n):
    arr = []
    while n > 0:
        n_new = n % 10
        n = n // 10
        arr.append(n_new)
    count = 1
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j] != arr[i]:
                count += 1
                i = j
        break
    return count

print(f(n))


def f(n):
    prev = None
    count = 0
    while n > 0:
        curr = n % 10
        n //= 10
        if curr != prev:
            count += 1
        prev = curr
    return count
