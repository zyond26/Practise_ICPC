from itertools import product

def find(N, k, A):
    b = []
    
    for i in range(N):
        for j in range(N):
            for p in range(N):
                for q in range(N):
                    if A[i] & A[j] & A[p] & A[q] == 0:
                        b.append((i + 1, j + 1, p + 1, q + 1))  
    
    b.sort()
    
    if k > len(b):
        return -1
    
    return b[k - 1]

N, k = map(int, input().split())
A = list(map(int, input().split()))

result = find(N, k, A)

if result == -1:
    print(-1)
else:
    print(*result)
