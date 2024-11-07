INF = float('inf')
n, m = map(int, input().split())
cost = [[INF] * n for _ in range(n)]

# Nhập chi phí giữa các thành phố
for _ in range(m):
    i, j, c = map(int, input().split())
    cost[i-1][j-1] = c

# Khởi tạo mảng dp với giá trị vô cực
dp = [[INF] * n for _ in range(1 << n)]
dp[1][0] = 0  # Bắt đầu từ thành phố đầu tiên với chi phí 0

# Tính dp[mask][i]
for mask in range(1 << n):
    for i in range(n):
        if mask & (1 << i):  # Nếu i đã được thăm trong mask
            for j in range(n):
                if mask & (1 << j) and cost[j][i] != INF:
                    dp[mask][i] = min(dp[mask][i], dp[mask ^ (1 << i)][j] + cost[j][i])

# Tìm chi phí nhỏ nhất để hoàn thành hành trình
result = INF
for i in range(1, n):
    if cost[i][0] != INF:
        result = min(result, dp[(1 << n) - 1][i] + cost[i][0])

print(result if result != INF else -1)
