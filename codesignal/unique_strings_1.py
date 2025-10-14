# You are given a string s and an integer array indices of the same length. You must reorder the string s such that the character at the i-th position moves to indices[i] in the reordered string.
s = "code"
indices = [3, 0, 2, 1]
# the thing we have in indeces are an indexing scheme for the s, we should then arrange it normally, not that we take normal indexes from s and put those numbers into indices positions
def f(s, indices):
    reord = ""
    for j in indices:
        for i in range(len(s)):
            if i == j:
                reord += s[i]
    return reord

print(f(s, indices))

def f(s, indices):
    reord = [""] * len(s)
    for i in range(len(s)):
        reord[indices[i]] = s[i]
    return "".join(reord)

print(f("code", [3,0,2,1]))  # prints: odec
