# Given a string s, iterate through it and return the total count of uppercase English letters ('A' through 'Z').
s = "Hello World"
count = 0
for char in s:
    if char.isupper():
        count += 1
print(count)