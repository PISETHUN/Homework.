def number(array):
    count = 0
    for i in range(len(array)):
            if array[i] ==5:
                count += 1
    return count
array_number = [2,3,5,0,11,5,2]
print(number(array_number))