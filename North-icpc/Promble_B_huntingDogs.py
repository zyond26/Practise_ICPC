def max_market_value(n, dogs):
    dogs.sort(key=lambda x: (x[0], -x[1]))
    
    from collections import defaultdict
    dp = defaultdict(int)
    max_value = 0

    for weight, intelligence, market_value in dogs:
        current = {}

        for i, v in dp.items():
            if intelligence >= i:  
                current[intelligence] = max(current.get(intelligence, 0), v + market_value)
        
        current[intelligence] = max(current.get(intelligence, 0), market_value)
        
        for i, v in current.items():
            dp[i] = max(dp[i], v)

        max_value = max(max_value, dp[intelligence])

    return max_value

n = int(input())
dogs = []
for _ in range(n):
    weight, intelligence, market_value = map(int, input().split())
    dogs.append((weight, intelligence, market_value))

print(max_market_value(n, dogs))
