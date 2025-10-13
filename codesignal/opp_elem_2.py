#Given a string s, determine if it is a palindrome after converting all uppercase letters into lowercase and removing all non-alphanumeric characters. Return true if it is a palindrome, or false otherwise.
s = "race a car"
def palindrome(s):
    s_lo = s.lower()
    new_s = ""
    for i in s_lo:
        if i.isalnum():
            new_s += i
    if new_s == new_s[::-1]:
        return True
    return False

print(palindrome(s))