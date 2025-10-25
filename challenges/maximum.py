numbers = [34, 54, 78, 343, 545,999, 223]
maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
print(maximum)


#find maximum using function
def find_max(list):
    maximum = list[0]
    for number in list:
        if number > maximum:
            maximum = number
    return maximum

