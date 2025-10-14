# This task directly corresponds to Circular Character Jump in a String.
#Problem: You are given a string s and an integer k (the jump size). Starting from index 0, you must build a new string by picking every k-th character from s in a circular manner until you have picked s.length characters.
#A circular jump means that if an index goes past the end of the string, it wraps around to the beginning.
s = "abcd"
k = 2

def f(s,k):
    l = ""
    i = 0
    for _ in range(len(s)):
        l += s[i]
        i =  (i + k) % len(s) #circular motion
    return l

print(f(s,k))
