def wood_cut(arr, N, H):
    total_wood = 0
    for height in arr:
        if height > H:  
            total_wood += height - H
        if total_wood >= M:  
            return total_wood
    return total_wood

def find_max_saw_height(arr, N, M):
    low, high = 0, max(arr)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
 
        if wood_cut(arr, N, mid) >= M:
            result = mid  
            low = mid + 1  
        else:
            high = mid - 1  
    
    return result

N, M = map(int, input().split())
arr = list(map(int, input().split()))

print(find_max_saw_height(arr, N, M))
