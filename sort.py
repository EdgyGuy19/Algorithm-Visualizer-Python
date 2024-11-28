import random

arrsize = 50
array = [random.randint(1, arrsize) for _ in range(arrsize)]

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

def main():
    print("Original array:")
    print(array)

    # Insertion Sort
    arr_insertion = array.copy()
    insertion_sort(arr_insertion)
    print("\nArray after Insertion Sort:")
    print(arr_insertion)

    # Selection Sort
    arr_selection = array.copy()
    selection_sort(arr_selection)
    print("\nArray after Selection Sort:")
    print(arr_selection)

if __name__ == "__main__":
    main()