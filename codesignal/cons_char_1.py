#You are given an alphanumeric string s. Implement a function to perform basic run-length encoding. This means for each group of consecutive identical characters, you should append the character followed by its count.
#Return the compressed string.
s = "aaabbbccc"
def f(s):
    char_length = 0
    curr_char = None
    result = []
    for i in s:
        if i == curr_char:
            char_length += 1
        else:
            if curr_char != None:
                result.append((curr_char, char_length))
            curr_char = i
            char_length = 1
    if curr_char != None:
        result.append((curr_char, char_length))
    return result

print(f(s))
