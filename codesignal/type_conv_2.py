# You are given a string number representing a phone number that contains digits, spaces, and dashes. You want to reformat the number into a specific pattern.
#First, remove all spaces and dashes. Then, group the digits from left to right into blocks of three, separated by dashes. The very last block may have two, three, or four digits.

number = "1-23-45 6"
numb_sort = []
for i in number:
    if i.isalnum():
        numb_sort.append(i)
no = "".join(numb_sort)
print(no)
j = 0

#SKIPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP