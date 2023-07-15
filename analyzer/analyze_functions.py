class analyze_functions:
    def __init__(self):
        pass
    def count_conflicts_by_mergeSort(self,arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            self.count_conflicts_by_mergeSort(L)
            self.count_conflicts_by_mergeSort(R)
            i = j = k = swaps = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                    swaps += len(L) - i
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
            return swaps
        else:
            return 0
    def count_conflicts_by_bubbleSort(self,arr):
        n = len(arr)
        swaps = 0
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swaps += 1
        return swaps
    def analyze_time_score(self,time,amount):
        return amount/time
