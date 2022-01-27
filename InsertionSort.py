def insertionSort(list):
    for j in range(2,len(list)):
        key = list[j]
        i = j - 1
        while i>=0 and list[i] > key:
            list[i+1] = list[i]
            i = i - 1
        list[i+1] = key
    print("The sorted list = " + str(list))
list = []
print("Enter the unsorted array")
for k in range(0,5):
    a = input("Enter the element : ")
    list.append(a)
print("The unsorted list = " + str(list))
insertionSort(list)