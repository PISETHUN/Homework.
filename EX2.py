def sum(array):
    sum = 0
    for i in range(len(array)):
        if array[i] != ' ':
            if (array[i]) % 2 == 1:
                sum += (array[i])
    return sum
array_number = [1,2,3,4,5,6]
print(sum(array_number))