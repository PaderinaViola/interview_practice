# Given a string s, reverse the characters for every consecutive group of three characters. If the last group has fewer than three characters, reverse it as well.
#slicing? like [i:i+3], so now after creating one subgroup (it was correct), we should create the next one in the same variable
s = "abcdefghuk"
def f(s):
    subgroup = ""
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        subgroup += group[::-1]
    return subgroup
print(f(s))