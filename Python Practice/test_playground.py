num = 38
output = 0
numString = str(num)
while len(str(output)) == 1:
    for i in numString:
        i = int(i)
        output += i

    numString = str(output)
    print(output)
    continue
print(output)