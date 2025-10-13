#You are given an array of integers stream representing a data stream. The stream officially ends when the number -1 is encountered. Calculate the sum of all valid data points that appear before the stream ends.
#A valid data point is any number between 0 and 100, inclusive.
#Data points outside the 0-100 range are invalid and should be skipped 
#Processing must stop immediately with break when -1 is found.
stream = [10, 20, 105, 30, -5, -1, 40]
total = 0
for i in stream:
    if i == -1:
        break
    elif 0 <= i and 100 >= i:
        total += i
    else:
        continue
print(total)
    