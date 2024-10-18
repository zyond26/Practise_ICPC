def marble_sorting(n, w, a, b):
    pos = {b[i]: i for i in range(n)}  
    visited = [False] * n  
    total_cost = 0  
    global_min = min(w)  
    for i in range(n):
        if visited[i]: 
            continue
        
        cycle_sum = 0  
        cycle_min = float('inf')  
        cycle_len = 0  
        x = i
        
        while not visited[x]:
            visited[x] = True  
            color = a[x] - 1  
            cycle_sum += w[color]  
            cycle_min = min(cycle_min, w[color])  
            cycle_len += 1  
            x = pos[a[x]]  
        
        if cycle_len > 1:
            option1 = cycle_sum + (cycle_len - 2) * cycle_min
            option2 = cycle_sum + cycle_min + (cycle_len + 1) * global_min
            total_cost += min(option1, option2)
    
    return total_cost

n = int(input())
w = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(marble_sorting(n, w, a, b))
