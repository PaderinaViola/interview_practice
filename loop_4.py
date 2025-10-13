# Given an array of strings words, create and return a single string by concatenating the elements, separated by a comma. The returned string must not have a comma at the end. If the input array is empty, return an empty string.
words = ["LeetCode", "is", "fun"]
def problem(words):
    total = ''
    for i in words:
        total += f"{i},"
    return total
    
print(problem(words))

def problem(words):
    # The .join() method takes an iterable (like a list) and
    # joins its elements with the string it's called on.
    return ",".join(words)

words = ["LeetCode", "is", "fun"]
print(problem(words)) # Output: "LeetCode,is,fun"