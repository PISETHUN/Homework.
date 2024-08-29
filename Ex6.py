def number(array):
    count = 0
    for i in range(len(array)):
        if array[i] >= 0:
            count +=1
    return count
array_number = [-1,11,2,0,-1,4]
print(number(array_number))