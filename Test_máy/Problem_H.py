def sum_S(n, M):
    return (n * (n + 1) * (2 * n + 1) // 6) % M

def solve(A, B, M):
    sum_B = sum_S(B, M)
    sum_A = sum_S(A - 1, M) if A > 0 else 0
    return (sum_B - sum_A + M) % M

A, B, M = map(int, input().split())
print(solve(A, B, M))
