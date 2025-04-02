def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def has_three_sum(arr, P):
    n = len(arr)
    quicksort(arr, 0, n - 1)
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == P:
                return True
            elif s < P:
                left += 1
            else:
                right -= 1
    
    return False

print(has_three_sum([1, 2, 3], 6))