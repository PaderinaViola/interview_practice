#  Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
s = "A man, a plan, a canal: Panama"
def is_palindrome(s):
    clean = ''.join(char.lower() for char in s if char.isalnum())
    return clean == clean[::-1]

print(is_palindrome(s))