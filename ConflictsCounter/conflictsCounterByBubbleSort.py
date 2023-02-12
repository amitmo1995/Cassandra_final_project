def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps

arr = [3 ,4 ,1 ,2]
print("Number of swaps:", bubble_sort(arr))
print("Sorted array:", arr)