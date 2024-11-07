def count_triples_with_sum_k(arr, N, K):
    arr.sort()
    count = 0
    
    for i in range(N - 2):
        j, k = i + 1, N - 1
        
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            
            if total == K:
                count += 1
                j += 1
                k -= 1
            elif total < K:
                j += 1
            else:
                k -= 1
    
    return count

N, K = map(int, input().split())
arr = list(map(int, input().split()))

result = count_triples_with_sum_k(arr, N, K)
print(result)
