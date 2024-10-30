def max_sum(matrix, n, m, k):
    max_sum = 0
    found = False

    for r1 in range(n):
        col_sum = [0] * m
        for r2 in range(r1, n):
            for c in range(m):
                col_sum[c] += matrix[r2][c]
            dict = {0: -1}
            current_sum = 0
            for c in range(m):
                current_sum += col_sum[c]
                remainder = current_sum % k
                if remainder in dict:
                    found = True
                    sub_sum = current_sum - (dict[remainder] + 1) * k
                    max_sum = max(max_sum, sub_sum)
                else:
                    dict[remainder] = c
    return max_sum if found else 0

n, m, k = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(max_sum(matrix, n, m, k))
