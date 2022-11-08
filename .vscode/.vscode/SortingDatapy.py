def insertionSort(list):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(list)):
 
        key = list[i]
 
        j = i-1
        while j >= 0 and key < list[j] :
                list[j + 1] = list[j]
                j -= 1
                print(list)
        list[j + 1] = key
 
 
list = [0, 12, 14, 21, 2, 3, 1, 4, 9, 10, 34]
insertionSort(list)
print(list)