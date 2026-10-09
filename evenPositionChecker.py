
numbers = [3, 4 ,66, 78, 90, 12, 34, 56]

sumOfevenIndex = 0

for index in range(0, len(numbers)):

    if(index % 2 == 0):

        sumOfevenIndex += numbers[index]




print(sumOfevenIndex)
