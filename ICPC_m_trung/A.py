def max_thief_value(N, W, H, items):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    max_value = 0

    for i in range(N):
        wi, ci = items[i]
        
        current_weight = 0
        current_value = 0
        
        for j in range(N):
            if j != i:  
                wj, cj = items[j]
                if current_weight + wj <= W:
                    current_weight += wj
                    current_value += cj
        
        if wi <= H:
            max_value = max(max_value, current_value + ci)
        else:
            max_value = max(max_value, current_value)

    return max_value

N, W, H = map(int, input().split())
items = []

for _ in range(N):
    wi, ci = map(int, input().split())
    items.append((wi, ci))

result = max_thief_value(N, W, H, items)
print(result) 