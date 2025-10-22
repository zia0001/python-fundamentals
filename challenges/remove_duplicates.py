numbers = [4543,23,89,23,222,4543]
unique =[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)