def has_three_sum(arr, P):
    N = len(arr)

    for i in range(N - 1):
        seen = set()
        target = P - arr[i]
        
        for j in range(i + 1, N):
            if target - arr[j] in seen:
                return True
            seen.add(arr[j])        
    return False

print(has_three_sum([1, 1, 1], 3))