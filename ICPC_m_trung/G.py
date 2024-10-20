def count_shared_cells(M, N, p, q):
    row_start = max(1, p - 1)
    row_end = min(M, p + 1)
    col_start = max(1, q - 1)
    col_end = min(N, q + 1)
    
    count = 0
    for i in range(row_start, row_end + 1):
        for j in range(col_start, col_end + 1):
            if i == p and j == q:
                continue 
            count += 1
    
    return count

M, N = map(int, input().split())
p, q = map(int, input().split())

result = count_shared_cells(M, N, p, q)
print(result)
