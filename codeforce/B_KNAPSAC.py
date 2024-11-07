#  cách 1 . Quy hoạch động
n, b = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (b + 1)

for weight, value in items:
    for w in range(b, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[b])

