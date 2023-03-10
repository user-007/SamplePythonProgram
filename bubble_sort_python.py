# Bubble
def bubbleSortAlg(array):
    a = len(array)
    for i in range(a):
        for j in range(0, a - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


arr = [4, -2, 7, -3, 0, 1, 2]

bubbleSortAlg(arr)
print(arr)

