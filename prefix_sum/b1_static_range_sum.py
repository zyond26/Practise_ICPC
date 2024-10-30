n, q = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]


results = []
for _ in range(q):
    a, b = map(int, input().split())
    range_sum = prefix_sum[b] - prefix_sum[a - 1]
    results.append(range_sum)
    
print("\n".join(map(str, results)))

