def number(array):
    min = (array[0])
    for i in range(len(array)):
        if array[i] != ' ':
            if (array[i]) > min:
                min = (array[i])
    return min
array_number = [2,3,5,0,11,5,2]
print(number(array_number))