def max_sum(arr):
    l = arr[0]
    r = arr[0]
    
    for i in range(1, len(arr)):
        l = max(arr[i], l + arr[i])
        
        if l > r:
            r = l
    return r

n = int(input())
arr = list(map(int, input().split()))

if len(arr) != n:
    print("Error")
else:
    result = max_sum(arr)
    print(result)
