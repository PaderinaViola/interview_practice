# Given an array of strings commands, process them to calculate a final score. Start with a score of 0. For each command in the array:
# If the command is "ADD", add 1 to the score.
# If the command is "SUBTRACT", subtract 1 from the score.
# Any other command is considered invalid and should be ignored.
# Return the final score after processing all commands.

commands = ["ADD", "ADD", "INVALID", "SUBTRACT"]
score = 0
for i in commands:
    if i == "ADD":
        score += 1
    elif i == "SUBTRACT":
        score -= 1
    else:
        continue
print(score)