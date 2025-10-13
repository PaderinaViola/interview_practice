#Given a string s and an integer k, apply a rotational (Caesar) cipher to the string. Each English letter should be shifted k positions forward in the alphabet, wrapping around from z to a. Case should be preserved. Non-alphabetic characters should remain unchanged.
s = "middle-Outz"
k = 2
s_new = ""
for i in s:
    if i.isalpha():
        i_new = ord(i)
        char_new = i_new + k
        char_new = chr(char_new)
        s_new += char_new
    else:
        s_new += i
print(s_new)
#просто вручну прописати винятки

def rotational_cipher(text, key):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            start = ord('a')
            new_ord = (ord(char) - start + key) % 26 + start
            result.append(chr(new_ord))
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters
            start = ord('A')
            new_ord = (ord(char) - start + key) % 26 + start
            result.append(chr(new_ord))
        else:
            # Handle non-alphabetic characters
            result.append(char)
    
    return "".join(result)

s = "middle-Outz"
k = 2
print(rotational_cipher(s, k))
# Output: okffng-Qwvb