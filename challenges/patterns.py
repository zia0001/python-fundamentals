numbers = [5, 2, 5, 2, 2]

# for number in numbers:
#     print( "*" * number )

for i in numbers:
    output = ''
    for j in range(i):
        output += '*' 
    print(output)
    
    
# L shape

nums = [1, 1, 1, 1, 5]
for i in nums:
    output = ''
    for j in range(i):
        output += '$'
    print(output)