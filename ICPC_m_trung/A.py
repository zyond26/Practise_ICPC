def thief(N, W, H, items):
    dp = [0] * (W + 1)
    
    for wi, ci in items:
        for w in range(W, wi - 1, -1):
            dp[w] = max(dp[w], dp[w - wi] + ci)
    
    max_value = max(dp)
    
    for wi, ci in items:
        if wi <= H:
            max_value = max(max_value, max(dp) + ci)
    
    return max_value

N, W, H = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

print(thief(N, W, H, items))
