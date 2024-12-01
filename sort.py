import random

arrsize = 51
array = [random.randint(1, arrsize - 1) for _ in range(arrsize - 1)]
array.append(55) #for testint the search algorithms

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def selection_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]

def heap_sort(array):
    n = arrsize
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1,0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)

def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left
    
    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        heapify(array, n, largest) 

def merge_sort(array, left, right):
    if right <= left:
        return
    half = (right + left) // 2

    merge_sort(array, left, half)
    merge_sort(array, half + 1, right)
    merge(array, left, half, right)

def merge(array, left, half, right):
    temparr = []
    index1 = left
    index2 = half + 1

    while index1 <= half and index2 <= right:
        if array[index1] < array[index2]:
            temparr.append(array[index1])
            index1 += 1
        else:
            temparr.append(array[index2])
            index2 += 1
    while index1 <= half:
        temparr.append(array[index1])
        index1 += 1
    while index2 <= left:
        temparr.append(array[index2])
        index2 += 1
    for i in range(0, len(temparr)):
        array[left + i] = temparr[i]

def bubble_sort(array):
    for i in range(0, arrsize - 1):
        for j in range(0, arrsize - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def linear_search(array, value):
    for i in range(0, arrsize):
        if array[i] == value:
            return i
    return -1

def binary_search(array, low, high,value):
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == value:
            return mid
        
        if array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    print("Original array:")
    print(array)

    # Sorting Algorithms
    arr_sorted = array.copy()
    insertion_sort(arr_sorted)
    print("\nArray after Insertion Sort:", arr_sorted)

    arr_sorted = array.copy()
    selection_sort(arr_sorted)
    print("\nArray after Selection Sort:", arr_sorted)

    arr_sorted = array.copy()
    heap_sort(arr_sorted)
    print("\nArray after Heap Sort:", arr_sorted)

    arr_sorted = array.copy()
    merge_sort(arr_sorted, 0, len(arr_sorted) - 1)
    print("\nArray after Merge Sort:", arr_sorted)

    arr_sorted = array.copy()
    bubble_sort(arr_sorted)
    print("\nArray after Bubble Sort:", arr_sorted)

    # Searching Algorithms
    value = 55
    print(f"\nLinear Search result for {value}: Index {linear_search(array, value)}")
    print(f"Binary Search result for {value}: Index {binary_search(arr_sorted, 0, len(arr_sorted) - 1, value)}")

if __name__ == "__main__":
    main()