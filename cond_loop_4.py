#Given an array of strings inputs representing user keyboard entries, validate them. If an entry is "STOP", immediately terminate the validation process. If an entry's length is less than 3 characters, it's considered invalid. Return the total count of valid entries processed before a "STOP" command is encountered.
inputs = ["start", "ok", "run", "hackyeah", "STOP", "end"]
count = 0
for i in inputs:
    if i == "STOP":
        break
    elif len(i) >= 3:
        count += 1
print(count)