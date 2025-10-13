# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit. Return the single-digit result.
def problem(num):
    num_str = str(num)
    while len(num_str) > 1:
        num_str = "+".join(num_str)
        num_str = eval(num_str)
        num_new = num_str
        num_str = str(num_str)
    return num_new

print(problem(98))

def problem(num):
    # The outer loop runs as long as the number has more than one digit.
    while num >= 10:
        current_sum = 0
        # The inner loop sums the digits of the current number.
        while num > 0:
            current_sum += num % 10  # Get the last digit
            num //= 10             # Remove the last digit
        num = current_sum # Update num for the next outer loop check.
    return num

print(problem(98)) # Output: 8
print(problem(7))  # Output: 7