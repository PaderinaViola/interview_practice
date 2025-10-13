#Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space. Note that s may have leading or trailing spaces or multiple spaces between words. The returned string should only have a single space separating the words and no extra spaces.
s = "  the sky is blue  "
array = []
s_new = s.strip()
s_new = s.split()
for i in s_new:
    s_new.append(i)
    s_new.remove(i)
print(s_new)